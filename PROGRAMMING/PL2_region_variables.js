// variables, Let and Const

function deployResources(isProduction) {
    let region = 'us-east-1a'; // default region for development

    if (isProduction) {
        let region = 'us-east-1b'; // region for production
        console.log (`Deploying production resources in ${region}`);
        // Deploy production-specific resources here
    }

    console.log (`Setting up monitoring in ${region}`);
    // Set up monitoring here
}

deployResources (true); // Deploy for production
deployResources (false); // Deploy for development