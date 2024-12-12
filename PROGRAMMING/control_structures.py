# Control structures / Control Flow
instance_running = "running"

# If statements
if instance_running == "running":
    print("The ec2 is running")
elif instance_running == "stopped":
    print("The ec2 is stopped")
else:
    print("The ec2 is in an unexpected state")

# S3  Pulic Access Control structures / Control Flow
s3_bucket_public_access_block = "Allow"

# If statements
if s3_bucket_public_access_block == "Allow":
    print("The public access to the s3 bucket is: Allowed")
elif s3_bucket_public_access_block == "Block":
    print("The public access to the s3 bucket is: Blocked...")
else:
    print("The public access to the s3 bucket is in an unexpected or unknown state")

