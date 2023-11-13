import boto3

AWS_REGION = "ap-south-1"
bucket_name = "python-aws-learning-bucket-resource"


# Deleting S3 Buckets using Boto3 client
client = boto3.client('s3', region_name=AWS_REGION)
client.delete_bucket(Bucket=bucket_name)
print(bucket_name, ' -- Bucket deleted')

# Deleting S3 Buckets using Boto3 resource
# resource = boto3.resource('s3', region_name=AWS_REGION)
# bucket = resource.Bucket(bucket_name)
# bucket.delete()

