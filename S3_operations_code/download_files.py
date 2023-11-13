import boto3

# AWS region, S3 bucket name, and local file path
AWS_REGION = "ap-south-1"
S3_BUCKET_NAME = "python-aws-learning-bucket"
LOCAL_FILE_PATH = "/AWS/downloaded_from_s3/test.txt"

# Creating an S3 client in the specified region
s3_client = boto3.client("s3", region_name=AWS_REGION)

try:
    # Downloading the 'generated.txt' file from S3 to the specified local file path
    s3_client.download_file(S3_BUCKET_NAME, 'generated.txt', LOCAL_FILE_PATH)
    
    print(f'S3 object downloaded to {LOCAL_FILE_PATH}')
except Exception as e:
    print(f'Error: {str(e)}')
