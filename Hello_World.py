def lambda_handler(event, context):
    """
    AWS Lambda function handler.

    Args:
    - event: The event data that triggers the Lambda function.
    - context: Information about the invocation, function, and runtime environment.

    Returns:
    - dict: A response object containing a status code and a message.
    """
    print("Hello, Militooo! The Lambda function was triggered.")
    
    # Example response
    response = {
        "statusCode": 200,
        "body": "Hello, World! Welcome to AWS Lambda!"
    }
    
    return response
