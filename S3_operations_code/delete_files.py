import boto3

AWS_REGION = "ap-south-1"
S3_BUCKET_NAME = "python-aws-learning-bucket"
s3_resource = boto3.resource("s3", region_name=AWS_REGION)
s3_object = s3_resource.Object(S3_BUCKET_NAME, 'test1.txt')

s3_object.delete()
print('S3 object deleted')
