import json
import handaler

def lambda_handler(event, context):
    if event['httpMethod'] == 'POST':
        resault, statusCode = handaler.post(event)
    else:
        resault, statusCode = {'ok': 'Hello From SMAM Lambda Function'}, 200
    return {
        'statusCode': statusCode,
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
        },
        'body': json.dumps(resault)
    }