import boto3
import io
import re
from datetime import datetime

# --- Configuration ---
bucket_name = "naomtech-versioned-bucket-002"
base_filename = "sample_report.txt"  # Base file name
new_file_content = "This is dynamically generated content version2"  # Content you want to upload

# --- Create S3 client ---
s3 = boto3.client("s3")


# --- Step 1: Get all existing versioned files ---
def get_existing_versions(bucket, base_filename):
    base_name, ext = base_filename.rsplit('.', 1)
    response = s3.list_objects_v2(Bucket=bucket, Prefix=base_name)

    versions = []
    if "Contents" in response:
        for obj in response["Contents"]:
            key = obj["Key"]
            match = re.search(rf"{base_name}_v(\d+)\.{ext}$", key)
            if match:
                versions.append((int(match.group(1)), key))
    return sorted(versions, key=lambda x: x[0])  # sort by version number


# --- Step 2: Check if latest version exists and compare content ---
existing_versions = get_existing_versions(bucket_name, base_filename)
create_new_version = True

if existing_versions:
    latest_version_num, latest_key = existing_versions[-1]
    # Fetch content of latest version
    latest_obj = s3.get_object(Bucket=bucket_name, Key=latest_key)
    latest_content = latest_obj['Body'].read().decode('utf-8')

    if latest_content == new_file_content:
        print(f"⚠️ Content is identical to latest version ({latest_key}). No new version created.")
        create_new_version = False
        dynamic_filename = latest_key
        version_num = latest_version_num

if create_new_version:
    # Step 3: Determine next version
    version_num = (existing_versions[-1][0] + 1) if existing_versions else 1
    dynamic_filename = f"{base_filename.rsplit('.', 1)[0]}_v{version_num}.txt"

    # Step 4: Upload new content from memory
    file_obj = io.BytesIO(new_file_content.encode('utf-8'))
    s3.upload_fileobj(file_obj, bucket_name, dynamic_filename)
    print(f"✅ Uploaded new version: {dynamic_filename}")

# --- Step 5: Fetch metadata ---
metadata = s3.head_object(Bucket=bucket_name, Key=dynamic_filename)
file_info = {
    "BucketName": bucket_name,
    "FileName": dynamic_filename,
    "CustomVersion": f"_v{version_num}",
    "AWSVersionId": metadata.get("VersionId"),
    "Size": metadata.get("ContentLength"),
    "LastModified": str(metadata.get("LastModified"))
}

print("\n📘 File Metadata:")
print(file_info)
