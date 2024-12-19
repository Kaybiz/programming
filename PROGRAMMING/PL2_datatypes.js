// Data types in JavaScript


// 1 ----- Number -----
const instanceCount = 5;
const cpuUtilization = 75.5;

console.log(typeof instanceCount); // Outputs: number
console.log(typeof cpuUtilization); // Outputs: number

// 2 ----- String -----
const region = 'us-east-1'
const errorMessage = 'Resource not found'
const logEntry = `Deployment failed in ${region}: ${errorMessage}`; 

console.log(typeof region); // Outputs: string

// 3 ----- Boolean -----
const isProduction = true;
const debugMode = false;

console.log(typeof isProduction); // Outputs: Boolean

if (isProduction && !debugMode) {
    console.log("Running in production mode");
}

// 4 ----- Undefined -----
let configFile;
console.log(typeof configFile); // Outputs: Undefined

if (configFile === undefined) {
    console.log("Config file is not loaded");
    // Load config file here
}

// 5. ----- Null -----
const cacheResult = null;
console.log(typeof cacheResult); // Outputs: object {this is a known javaScript quirk}
if (cacheResult === null) {
    console.log("No data in cache, fetching from database");
    // Fetch data from database
}

// 6 ----- Object Literals -----
const ec2Instance = {
    instanceId: 'i-12346abcdef0',
    type: 't2.micro',
    state: 'running',
    launchTime: new Date('2023-09-15T10:00:00Z')
}
console.log(typeof ec2Instance); // Outputs: object
console.log(ec2Instance.type); // Outputs t2.micro

// 7 ----- Arrays -----
const availabilityZones = ['us-east-1a', 'us-east-1b', 'us-east-1c'];
console.log(typeof availabilityZones); // Outputs: object
console.log(Array.isArray(availabilityzones)); // Outputs: true

availabilityZones.forEach(zone => {
    console.log('Deploying to ${zone}');
})




let x = 5; //number 
const y = 3.14; // number
var name = "Kayode"; // string
let isvalid = true; // boolean 