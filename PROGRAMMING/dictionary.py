# EC2 
ec2_instance = {
    "InstanceId": "i-123456abcde",
    "InstanceType": "t2.micro",
    "State": "running",
    "PublicIpAddress": "203.0.111.2"
}
# This dictionary represents an EC2 instance with 4 main attributes
# such as InstanceId, InstanceType, State, and PublicIpAddress
# Each key value pair in a dictionary corresponds to the property of the instance

instance_id = ec2_instance ["InstanceId"]
print(f"this is a {instance_id} instance")

public_ip = ec2_instance.get("PublicIpAddress", "No Public IP address is here")
print(f"the instances public Ip is: {public_ip}")

# Adding a new key value pair to the dictionary
ec2_instance["AvailabilityZone"] = "us-east-1a"
ec2_instance["state"]="stopped"

print(ec2_instance)

# Removing a key value pair from the dictionary using pop ()method
rm_instance_type = ec2_instance.pop("InstanceType")
print(f"removed instance type: {rm_instance_type}")
print(ec2_instance)

# Removing a key value pair from the dictionary del ()method
del ec2_instance["AvailabilityZone"]
print(ec2_instance)
