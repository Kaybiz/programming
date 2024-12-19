// --- Basic Functions ----
  
function sayHello () {
    console.log("Hello, Cloud Engineer!");
  }

  // --- Calling Function ---
  sayHello();

  // --- Function Parameters ----
  function deployToRegion(region) {
    console.log("Deploying to region: " + region);
  }

// Calling Function with Parameters
deployToRegion("us-west-2");

// ConfigureService

function configureService (serviceName, tier) {
    console.log("Configuring " + serviceName + " service with tier: " + tier);
}

// Calling configureService Function with Parameters
configureService ("EC2", "t2.micro")
configureService ("S3", "standard")
