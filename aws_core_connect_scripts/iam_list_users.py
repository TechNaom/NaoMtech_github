import boto3

iam = boto3.client('iam')
response = iam.list_users()

print("IAM Users:")
for user in response['Users']:
    print(f"- {user['UserName']} (Created: {user['CreateDate']})")


response2 = iam.list_roles()
print("IAM Roles:")
for role in response2['Roles']:
        role_name = role['RoleName']
        role_arn = role['Arn']
        create_date = role['CreateDate']
        assume_role_policy = role['AssumeRolePolicyDocument']

        print(f"Role Name: {role_name}")
        print(f"ARN: {role_arn}")
        print(f"Created On: {create_date}")
        print(f"Assume Role Policy: {assume_role_policy}")
        print("-" * 50)