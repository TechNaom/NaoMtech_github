import boto3

iam = boto3.client('iam')

response = iam.list_users()

print("IAM Users:")
for user in response['Users']:
    print(f"- {user['UserName']} (Created: {user['CreateDate']})")
