import boto3
import json
import re  # for pattern matching

# Create S3 client
s3 = boto3.client('s3')
bucket_name = 'naomtech-versioned-bucket-002'

# Step 1: Fetch object versions
response = s3.list_object_versions(Bucket=bucket_name)

# Step 2: Filter keys containing pattern like _v1, _v2, _v10, etc.
filtered_versions = [
    v for v in response.get('Versions', [])
    if re.search(r'_v\d+', v.get('Key', '').lower())
]

# Step 3: Loop and print metadata for each filtered version
for v in filtered_versions:
    meta = s3.head_object(
        Bucket=bucket_name,
        Key=v['Key'],
        VersionId=v['VersionId']
    )

    print(f"Key: {v['Key']}")
    print(f"AWS VersionId: {v['VersionId']}")
    print(f"Size: {meta['ContentLength']} bytes")
    print(f"Last Modified: {meta['LastModified']}")
    print("-" * 60)
