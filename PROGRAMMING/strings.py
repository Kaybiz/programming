# Single quotes
single_quotes = 'This is an EC2'

# Double quotes
double_quotes = "This is an s3 bucket"

# Tripple quotes for multi-line strings
multi_line = """"
This is a cloudformation template
which has multiple lines
"""
print (single_quotes)
print (double_quotes)
print (multi_line)

# Exercise
# 1. Single quoted string for an AWS region name

aws_region = 'us-east-1'

# 2. Double quoted string for an AWS an ec2 instance type

ec2_instance_type = "t2.micro"

# 3.Tripple quotes Multi-line string for a simple IAM policy
iam_policy = """"
{ 
    "Version": "2012-10-17"
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "s3:ListBucket",
            "Resource": "arn:aws:s3::example-bucket"
        }
    ]

"""
print (aws_region)
print (ec2_instance_type)
print(iam_policy)


