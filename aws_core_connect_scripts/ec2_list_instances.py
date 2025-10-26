import boto3

ec2 = boto3.client('ec2', region_name='ap-south-1')
response = ec2.describe_instances()

if not response['Reservations']:
    print("No EC2 instances found in this region.")
else:
    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            instance_id = instance['InstanceId']
            state = instance['State']['Name']
            tags = instance.get('Tags', [])
            name_tag = next((tag['Value'] for tag in tags if tag['Key'] == 'Name'), "No Name")

            print(f"Instance ID: {instance_id}")
            print(f"State: {state}")
            print(f"Name: {name_tag}")
            print("-" * 30)
