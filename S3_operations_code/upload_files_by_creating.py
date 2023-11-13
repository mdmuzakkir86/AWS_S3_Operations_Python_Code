import boto3
import io

# AWS region and S3 bucket name
AWS_REGION = "ap-south-1"
S3_BUCKET_NAME = "python-aws-learning-bucket"

# Creating an S3 client in the specified region
s3_client = boto3.client("s3", region_name=AWS_REGION)

# Function to upload a generated file object to S3
def upload_generated_file_object(bucket, object_name):
    # Creating an in-memory BytesIO object
    with io.BytesIO() as f:
        # Writing content to the in-memory object
        f.write(b'First line.\n')
        f.write(b'Second line.\n')
        
        # Resetting the file pointer to the beginning of the file
        f.seek(0)
        
        # Using the S3 client to upload the in-memory file object to the specified S3 bucket
        s3_client.upload_fileobj(f, bucket, object_name)
        
        # Printing a message indicating that the generated file has been uploaded
        print(f"Generated file '{object_name}' has been uploaded to '{bucket}'")

# Calling the function to upload a generated file to S3
upload_generated_file_object(S3_BUCKET_NAME, 'generated.txt')
