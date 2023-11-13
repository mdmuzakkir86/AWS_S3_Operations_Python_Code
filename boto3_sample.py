# Connecting to AWS
import json
import boto3

# Create an AWS session
session = boto3.session.Session()

# Create an IAM resource using the session
# If we use resource we must pass service o name as parameter, I mean can't provide sts
iam_resource = session.resource('iam')

# Iterate over IAM users and print details
for user in iam_resource.users.all():
    print(f"User Name: {user.user_name}")
    print(f"User ARN: {user.arn}")
    print(f"User ID: {user.user_id}")
    print("-------------")


print(dir(session))
print(session.get_available_resources())

print("======================")

client = boto3.client('sts')
response = client.get_caller_identity()
print(response)
user_id = response['UserId']
account = response['Account']
arn = response['Arn']
output = {
    'UserId': user_id,
    'Account': account,
    'Arn': arn
}
print(json.dumps(output, indent=4))

print("======================")


import boto3
client = boto3.client('iam')
paginator = client.get_paginator('list_roles')
aws_roles = []
for page in paginator.paginate():
    for role in page['Roles']:
        aws_roles.append(role['RoleName'])
print('\n'.join(aws_roles))
print("==================")


iam_resource = boto3.resource('iam')
aws_roles = []
for role in iam_resource.roles.all():
    aws_roles.append(role.name)
print('\n'.join(aws_roles))
