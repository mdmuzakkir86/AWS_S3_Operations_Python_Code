import boto3

# AWS region and S3 bucket name
AWS_REGION = "ap-south-1"
S3_BUCKET_NAME = "python-aws-learning-bucket"

# Creating an S3 resource in the specified region
s3_resource = boto3.resource("s3", region_name=AWS_REGION)

# Function to rename an S3 object
def rename_s3_object(bucket_name, old_name, new_name):
    # Creating references to the old and new S3 objects
    old_s3_object = s3_resource.Object(bucket_name, old_name)
    new_s3_object = s3_resource.Object(bucket_name, new_name)

    # Copying the content from the old S3 object to the new S3 object
    new_s3_object.copy_from(CopySource=f'{bucket_name}/{old_name}')

    # Deleting the old S3 object
    old_s3_object.delete()

    print(f'{bucket_name}/{old_name} -> {bucket_name}/{new_name}')

# Calling the function to rename an S3 object
rename_s3_object(S3_BUCKET_NAME, 'sample.txt', 'learning_s3.txt')
