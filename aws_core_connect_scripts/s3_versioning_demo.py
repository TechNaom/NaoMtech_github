import boto3
import json

# Step 1: Initialize S3 client
#s3 = boto3.client('s3')
s3 = boto3.client('s3', region_name='ap-south-1')

# Step 2: Define bucket name and region
bucket_name = 'naomtech-versioned-bucket-789'  # must be unique globally
region = 'ap-south-1'

'''
# Step 3: Create bucket
print("Creating bucket...")
s3.create_bucket(
    Bucket=bucket_name,
    CreateBucketConfiguration={'LocationConstraint': region}
)
print(f"✅ Bucket '{bucket_name}' created successfully.")

# Step 4: Enable versioning
print("Enabling versioning...")
s3.put_bucket_versioning(
    Bucket=bucket_name,
    VersioningConfiguration={'Status': 'Enabled'}
)
print(f"✅ Versioning enabled on '{bucket_name}'.")
'''
# Step 5: Upload multiple versions of the same file
file_key = 'demo.txt'
print("Uploading 5th versions of the same file...")

s3.put_object(Bucket=bucket_name, Key=file_key, Body='This is version 4')
#s3.put_object(Bucket=bucket_name, Key=file_key, Body='This is version 2')
#s3.put_object(Bucket=bucket_name, Key=file_key, Body='This is version 3')

print("✅ Uploaded 3 versions successfully.")

# Step 6: List object versions
print("\nListing all versions in the bucket...")
response = s3.list_object_versions(Bucket=bucket_name)

print(json.dumps(response['Versions'], indent=2, default=str))
