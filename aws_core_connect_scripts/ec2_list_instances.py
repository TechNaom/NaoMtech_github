import boto3

ec2 = boto3.client('ec2')

response = ec2.describe_instances()

print("EC2 Instances:")
for reservation in response['Reservations']:
    for instance in reservation['Instances']:
        instance_id = instance['InstanceId']
        state = instance['State']['Name']
        # Get Name tag if exists
        #name_tag = next((tag['Value'] for tag in instance.get('Tags', []) if tag['Key'] == 'Name'), None)
        #print(f"- ID: {instance_id}, State: {state}, Name: {name_tag}")
        # Get the tags for this instance (if any)
        tags = instance.get('Tags', [])

        # Default name if no tag found
        name_tag = "No Name"

        # Loop through all tags and find the one with Key = 'Name'
        for tag in tags:
            if tag['Key'] == 'Name':
                name_tag = tag['Value']

        # Print instance details clearly
        print(f"Instance ID: {instance_id}")
        print(f"State: {state}")
        print(f"Name: {name_tag}")
        print("-" * 30)  # line separator for readability

