# Importing the Boto3 library, which is the Amazon Web Services (AWS) SDK for Python.
import boto3

# Defining the AWS region to be used.
AWS_REGION = "ap-south-1"


bucket_name = "python-aws-learning-bucket"

# Creating S3 Bucket using Boto3 client
# A Boto3 client provides a low-level interface to AWS services.
# Creating an S3 client in the specified region.
client = boto3.client("s3", region_name=AWS_REGION)

# Creating a dictionary specifying the location constraint for the S3 bucket.
# The location constraint is the region where the S3 bucket will be created.
# If you don't mention location then default is region associated with your AWS credentials.
location = {'LocationConstraint': AWS_REGION}

# Using the S3 client to create the first bucket with the specified name and location constraint.
bucket = client.create_bucket(
    Bucket=bucket_name,
    CreateBucketConfiguration=location
)
print("Amazon S3 bucket has been created")


print("=============================")


bucket_name = "python-aws-learning-bucket-resource"

# A Boto3 resource provides a higher-level, more Pythonic interface to AWS services.
resource = boto3.resource("s3", region_name=AWS_REGION)

bucket = resource.create_bucket(
    Bucket=bucket_name,
    CreateBucketConfiguration=location
)

print("Amazon S3 bucket has been created")
