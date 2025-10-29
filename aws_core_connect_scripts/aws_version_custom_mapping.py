import boto3
import json
import re

# Create S3 client
s3 = boto3.client('s3')
bucket_name = 'naomtech-versioned-bucket-002'

# Step 1: Get all versions
response = s3.list_object_versions(Bucket=bucket_name)

# Step 2: Filter only versioned files (_v1, _v2, etc.)
filtered_versions = [
    v for v in response.get('Versions', [])
    if re.search(r'_v\d+', v.get('Key', '').lower())
]

# Step 3: Create mapping { custom_version: aws_version_id }
version_mapping = {}

# Step 4: Loop through and build mapping
for v in filtered_versions:
    key_name = v['Key']
    aws_version_id = v['VersionId']

    # Extract custom version part from filename (like _v1)
    match = re.search(r'_v\d+', key_name.lower())
    custom_version = match.group() if match else "unknown"

    # Store in dictionary
    version_mapping[custom_version] = aws_version_id

    # Print details (for reference)
    meta = s3.head_object(
        Bucket=bucket_name,
        Key=key_name,
        VersionId=aws_version_id
    )
    print(f"Key: {key_name}")
    print(f"AWS VersionId: {aws_version_id}")
    print(f"Custom Version: {custom_version}")
    print(f"Size: {meta['ContentLength']} bytes")
    print(f"Last Modified: {meta['LastModified']}")
    print("-" * 60)

# Step 5: Print the final mapping dictionary
print("\n📘 Custom Mapping (Custom Version → AWS VersionId):")
print(json.dumps(version_mapping, indent=2))
