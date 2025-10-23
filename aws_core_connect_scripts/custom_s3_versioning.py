import boto3
import os

# Initialize S3 client
s3 = boto3.client('s3')

# Configuration
bucket_name = "naomtech-versioned-bucket-002"
file_name = "D:\\NaoMtech\\DevOPS_aws\\sample_report.txt"


# Create custom version label
version_number = input("Enter custom version (e.g., v1, v2, v3): ")
key_name = f"{os.path.splitext(file_name)[0]}_{version_number}{os.path.splitext(file_name)[1]}"

try:
    s3.upload_file(file_name, bucket_name, key_name)
    print(f"✅ Uploaded {file_name} as {key_name} to {bucket_name}")
except Exception as e:
    print(f"❌ Error: {e}")


versions = s3.list_object_versions(Bucket='naomtech-versioned-bucket-002')['Versions']
for v in versions:
    meta = s3.head_object(
        Bucket='naomtech-versioned-bucket-002',
        Key=v['Key'],
        VersionId=v['VersionId']
    )
    print(f"Key: {v['Key']}")
    print(f"AWS VersionId: {v['VersionId']}")
    

versions = s3.list_object_versions(Bucket='naomtech-versioned-bucket-002')
print(versions)

for v,meta in versions.items():
    if 'Versions' in v:
        print(v,meta)
        for values in meta:
            print(values['Key'])
            print(values['VersionId'])














