import boto3
import os
import re
import sys
import json

# Initialize S3 client
s3 = boto3.client('s3')

# Configuration
bucket_name = "naomtech-versioned-bucket-002"
file_name = "D:\\NaoMtech\\DevOPS_aws\\sample_report.txt"
#split file name by (.) - the delimiter used here is the dot (.) in the file name.
output=os.path.splitext(file_name) #returns tuple with split tokens
print(output[0]) #value from 0th index
print(output[1]) #$value from 1st index

'''
# Create custom version label
version_number = input("Enter custom version (e.g., v1, v2, v3): ")
#key_name = f"{os.path.splitext(file_name)[0]}_{version_number}{os.path.splitext(file_name)[1]}"
key_name=output[0]+'_'+version_number+'_'+output[1]


try:
    s3.upload_file(file_name, bucket_name, key_name)
    print(f"✅ Uploaded {file_name} as {key_name} to {bucket_name}")
except Exception as e:
    print(f"❌ Error: {e}")
'''


response= s3.list_object_versions(Bucket='naomtech-versioned-bucket-002')

'''
# Print formatted output
print(json.dumps(versions, indent=2, default=str))

versions2 = s3.list_object_versions(Bucket='naomtech-versioned-bucket-002')['Versions']
print(json.dumps(versions2, indent=2, default=str))

for v in versions2:
    meta = s3.head_object(
        Bucket='naomtech-versioned-bucket-002',
        Key=v['Key'],
        VersionId=v['VersionId']
    )
    print(f"Key: {v['Key']}")
    print(f"AWS VersionId: {v['VersionId']}")
    
#creating a custom mapping for Natural version vs custom version
version_dict={}
'''

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













