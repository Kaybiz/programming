# List of EC2 instance
instance_ids = ["i-9011", "i-5678", "i-1234"]

# List of IP addresses for a security group
ip_addresses = ["10.0.0.1", "10.0.02", "10.0.0.3", "10.0.0.4"]

# List of availability zones in a region
availability_zones = ["us-east-1a", "us-east-1b", "us-east-1c"]


# Print the lists
print(f"EC2 instances to terminate: {instance_ids}")
print(f"First IP addresses: {ip_addresses}")
print(f"Number Availability Zones AZs: {availability_zones}")

# Add new EC2 instance to the list
instance_ids.append("i-3456")
print ("After adding a new instance ID")
print ("EC2 Instances:", instance_ids)

# Remove EC2 Instance IDS From the list
instance_ids.remove("i-1234")
print ("After removing an instance ID")
print ("EC2 Instances:", instance_ids)

# Check if an item or IP address exists and allowed in the list
if "10.0.0.4" in ip_addresses:
   print("Yes 10.0.0.4 is in and allowed")
else:
   print("No 10.0.0.4 is not in the allowed list")
print("IP Addresses:", ip_addresses)


# Slicing a list
# First two AZ
first_two_azs = availability_zones[:2]
print("First two AZs:", first_two_azs)

# Sorting Instance IDs
instance_ids.sort()
print("Sorted Ec2 Instances", instance_ids)


# Finding length of a list
number_of_ips = len(ip_addresses)
print(f"Number of IP addresses: {number_of_ips}")

# Accessing list of items by Index
first_az = availability_zones[0]
last_az = availability_zones[-1]
print(f"First AZ:", first_az)
print(f"Last AZ:", last_az)

