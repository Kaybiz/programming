// -- For Loops ---

let regions = ["us-east-1", "us-east-2", "us-west-1", "us-west-2"];

for (let i = 0; i < regions.length; i++) {
    console.log("Deploying to region: " + regions[i]);
}


//  Array of Cloud services

let cloudServices = ["EC2", "S3", "Lambda", "DynamoDB"];
for (let i = 0; i < cloudServices.length; i++) {
    console.log("Configuring AWS: " + cloudServices[i]);
}