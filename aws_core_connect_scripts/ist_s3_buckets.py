import boto3

# Create S3 client
s3 = boto3.client('s3')

# List all buckets
response = s3.list_buckets()

print("S3 Buckets in your account:")
for bucket in response['Buckets']:
    print(f"- {bucket['Name']}")
