import boto3
import json
import re

# Create S3 client
s3 = boto3.client('s3')
bucket_name = 'naomtech-versioned-bucket-002'

# Step 1: Get all object versions
response = s3.list_object_versions(Bucket=bucket_name)

# Step 2: Filter files having version numbers (_v1, _v2, etc.)
filtered_versions = [
    v for v in response.get('Versions', [])
    if re.search(r'_v\d+', v.get('Key', '').lower())
]

# Step 3: Prepare structured data
bucket_data = {
    "BucketName": bucket_name,
    "Files": []
}

# Step 4: Loop and collect info
for v in filtered_versions:
    key_name = v['Key']
    aws_version_id = v['VersionId']

    # Extract custom version from file name
    match = re.search(r'_v\d+', key_name.lower())
    custom_version = match.group() if match else "unknown"

    # Get metadata for each version
    meta = s3.head_object(
        Bucket=bucket_name,
        Key=key_name,
        VersionId=aws_version_id
    )

    file_info = {
        "FileName": key_name,
        "CustomVersion": custom_version,
        "AWSVersionId": aws_version_id,
        "Size": meta['ContentLength'],
        "LastModified": str(meta['LastModified'])
    }

    bucket_data["Files"].append(file_info)

# Step 5: Pretty print and save
print(json.dumps(bucket_data, indent=2))

# Optional: Save to a JSON file
with open("bucket_version_mapping.json", "w") as f:
    json.dump(bucket_data, f, indent=2)
