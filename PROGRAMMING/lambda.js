///This is a Lambda Funtion in JavaScript
//This lambda function simply logs the incoming events and return a simple Hello from Lambda. 
///This demonstrate how JavaScript can be used directly in the cloud with AWS Lambda.

exports.handler = async (event) =>{
    console.log ('Received event:', JSON.stringify(event, null, 2));

    const response = {
        statusCode: 200,
        body: JSON.stringify('Hello from Lambda!'),
    }

    return response;
}