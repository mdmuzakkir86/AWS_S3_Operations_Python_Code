import io
import boto3

# AWS region and S3 bucket name
AWS_REGION = "ap-south-1"
S3_BUCKET_NAME = "python-aws-learning-bucket"

# Creating an S3 resource in the specified region
s3_resource = boto3.resource("s3", region_name=AWS_REGION)

# Creating an S3 object reference for the specified file in the bucket
s3_object = s3_resource.Object(S3_BUCKET_NAME, 'generated.txt')

# Using an in-memory BytesIO object to download the content of the S3 object
with io.BytesIO() as f:
    # Downloading the content of the S3 object to the in-memory object
    s3_object.download_fileobj(f)
    
    # Resetting the file pointer to the beginning of the file
    f.seek(0)
    
    print(f'Downloaded content:\n{f.read()}')
