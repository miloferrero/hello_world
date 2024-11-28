def lambda_handler(event, context):
    """
    AWS Lambda handler function.
    
    Args:
    - event: The data that triggers the Lambda function (sent by API Gateway or other AWS services).
    - context: Provides runtime information about the Lambda invocation.
    
    Returns:
    - A dictionary with an HTTP status code and a body message.
    """
    print("¡Hola, Militooo! Lambda fue invocada con éxito.")  # Esto aparecerá en los logs de CloudWatch
    
    # Retornamos una respuesta HTTP con código 200 y un mensaje en el body
    return {
        "statusCode": 200,
        "body": "¡Hola, Militooo! Esto está funcionando desde AWS Lambda."
    }
