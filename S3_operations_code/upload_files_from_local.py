import boto3
from glob import glob

# AWS region and S3 bucket name
AWS_REGION = "ap-south-1"
S3_BUCKET_NAME = "python-aws-learning-bucket"

# Creating an S3 client in the specified region
s3_client = boto3.client("s3", region_name=AWS_REGION)

# Function to upload files to S3
def upload_files_to_s3(file, s3_bucket_name, object_name=None, args=None):
    # If object_name is not specified, use the original file name
    if object_name is None:
        object_name = file
    
    # Using the S3 client to upload the file to the specified S3 bucket with optional ExtraArgs
    s3_client.upload_file(file, s3_bucket_name, object_name, ExtraArgs=args)
    print(f"'{file}' has been uploaded to '{s3_bucket_name}'")


# Upload multiple txt files available in the current location
files = glob("*.txt")
for file in files:
    upload_files_to_s3(file, S3_BUCKET_NAME)

# Upload a single file with a different name
# upload_files_to_s3("test.txt", S3_BUCKET_NAME, object_name='sample.txt')

# Encrypt the file and upload
# upload_files_to_s3("test.txt", S3_BUCKET_NAME, 'test.txt', args={'ServerSideEncryption': 'AES256'})
