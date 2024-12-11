# Define the AWS account ID
account_id = "1234567891011"

# Define the project name
project_name = "cloud_engineer_academy"

#Concatenate strings to form the s3 bucket name
bucket_name = account_id + '-' + project_name + "-bucket"

# Print the resulting bucket name

print (f"S3 Bucket Name: {bucket_name}")

# Exercise EC2 STRING CONCATENATION

# Environment name prod, dev, staging
environment = "dev"

# Application name
application_name = "appserver"

# Instance number
instance_number = "02"

# Concatenate
ec2_instance_name = environment + '-' + application_name + "-ec2_instance-" + instance_number 

# Print
print ("EC2 Instance Name: "+ ec2_instance_name)
       