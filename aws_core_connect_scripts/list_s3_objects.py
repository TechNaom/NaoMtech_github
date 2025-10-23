import boto3

bucket_name = "naomtech-versioned-bucket-001"  # Replace with your bucket name

s3 = boto3.client('s3')
response = s3.list_objects_v2(Bucket=bucket_name)

print(f"Objects in bucket '{bucket_name}':")
if 'Contents' in response:
    for obj in response['Contents']:
        print(f"- {obj['Key']}")
else:
    print("Bucket is empty")
