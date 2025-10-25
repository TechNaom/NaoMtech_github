import boto3
import io
import re
from datetime import datetime

# --- Configuration ---
bucket_name = "naomtech-versioned-bucket-002"
base_filename = "test_report.txt"  # Base name of the file

# --- Create S3 Client ---
s3 = boto3.client("s3")


# --- Step 1: Determine next version dynamically ---
def get_next_version(bucket, base_filename):
    base_name, ext = base_filename.rsplit('.', 1)
    response = s3.list_objects_v2(Bucket=bucket, Prefix=base_name)

    max_version = 0
    if "Contents" in response:
        for obj in response["Contents"]:
            key = obj["Key"]
            match = re.search(rf"{base_name}_v(\d+)\.{ext}$", key)
            if match:
                version_num = int(match.group(1))
                max_version = max(max_version, version_num)
    return max_version + 1


# --- Step 2: Generate new file content dynamically ---
version = get_next_version(bucket_name, base_filename)
dynamic_filename = f"{base_filename.rsplit('.', 1)[0]}_v{version}.txt"
file_content = f"This is dynamically generated version {version} at {datetime.now()}"

# --- Step 3: Upload file from memory ---
file_obj = io.BytesIO(file_content.encode('utf-8'))
s3.upload_fileobj(file_obj, bucket_name, dynamic_filename)

print(f"✅ Uploaded file dynamically as: {dynamic_filename}")

# --- Step 4: Fetch uploaded file metadata ---
response = s3.head_object(Bucket=bucket_name, Key=dynamic_filename)
metadata = {
    "BucketName": bucket_name,
    "FileName": dynamic_filename,
    "CustomVersion": f"_v{version}",
    "AWSVersionId": response.get("VersionId"),
    "Size": response.get("ContentLength"),
    "LastModified": str(response.get("LastModified"))
}

print("\n📘 Uploaded File Metadata:")
print(metadata)
