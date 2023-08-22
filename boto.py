import boto3

ec2_client = boto3.client('ec2')

INSTANCE_ID = 'i-04cc3eb848c0a7f5f'

ec2_client.stop_instances(InstanceIds=[INSTANCE_ID])

print(f"Stopping instance {INSTANCE_ID}...")

waiter = ec2_client.get_waiter('instance_stopped')

print(f"Instance {INSTANCE_ID} is stopped.")

response = ec2_client.create_image(
    InstanceId=INSTANCE_ID,
    Name="My_Server_AMI",
    Description="AMI created from script",
    NoReboot=True
)

ami_id = response['ImageId']
print(f"AMI {ami_id} has been created.")
