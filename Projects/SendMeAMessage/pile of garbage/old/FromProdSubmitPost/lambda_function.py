import json

def lambda_handler(event, context):
    # Parse the request body
    request_body = event['body']
    data = dict(item.split('=') for item in request_body.split('&'))

    # Store the data in a dictionary
    my_dictionary = {}

    for key, value in data.items():
        my_dictionary[key] = value

    # Return the dictionary as the response
    response = {
        'statusCode': 200,
        'body': json.dumps(my_dictionary)
    }

    return response