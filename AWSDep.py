import boto3
client = boto3.client('ec2')
keypair_name = "siddhi"
resp = client.run_instances(ImageId='ami-0f65671a86f061fcd',
InstanceType='t2.micro',
KeyName=keypair_name,
MinCount=1,
MaxCount=1)
for instance in resp['Instances']:
    print(instance['i-0bdf18ee1d9533565'])