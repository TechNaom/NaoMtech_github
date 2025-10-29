import boto3

# Create STS client
sts = boto3.client('sts')

# Get caller identity
response = sts.get_caller_identity()

print("AWS Caller Identity:")
print(f"Account ID: {response['Account']}")
print(f"ARN: {response['Arn']}")
print(f"User ID: {response['UserId']}")

# Check if root or IAM user
if ":root" in response['Arn']:
    print("You are using the ROOT account!")
else:
    print("You are using an IAM user or role.")
