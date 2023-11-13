import boto3

AWS_REGION = "ap-south-1"


# Listing S3 Buckets using Boto3 client

client = boto3.client('s3', region_name=AWS_REGION)
response = client.list_buckets()
print('client_response',response)
print('Listing Amazon S3 Buckets')
for bucket in response['Buckets']:
    print(f"-- {bucket['Name']}")

print('=================================')

# Listing S3 Buckets using Boto3 resource
resource = boto3.resource('s3', region_name=AWS_REGION)
response = resource.buckets.all()
print('resource_response',response)
print("Listing Amazon S3 Bucket")
for bucket in response:
    print(f"-- {bucket.name}")

