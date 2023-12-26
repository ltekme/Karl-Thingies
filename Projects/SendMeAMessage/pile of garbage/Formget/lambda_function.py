import json
import boto3
from datetime import datetime


def dynamo(record, time):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('FormMessages')
    sumbitDate = time.strftime('%Y%m%d')
    clock = time.strftime('%H%M%S') + time.strftime('%f')[:2]
    record['submitDate'] = str(sumbitDate)
    record['submitTime'] = str(clock)
    try:
        table.put_item(Item=record)
        return f"Your message is saved to dynamo. Thank You."
    except Exception as ex:
        return f"oops... error saving message to dynamoDB. {ex}"


def lambda_handler(event, context):
    time = datetime.utcnow()
    statusCode = 500
    reply = json.dumps({'Fuck you': 'Pece of shit'})
    query_params = event.get('queryStringParameters', None)
    if query_params is None:
        statusCode = 400
        reply = json.dumps({'error': 'Missing parameters'})
    else:
        name = query_params.get('name', 'noName')
        msg = query_params.get('msg', 'noMessage')
        
        if name == 'noName' and msg == 'noMessage':
            statusCode = 400
            reply = json.dumps({'error': 'Invalid parameters'})
        elif len(name) > 50 or len(msg) > 300:
            reply = json.dumps({'nope': 'Message or Name Too long'})
        else:
            result = {
                'Name': str(name),
                'Message': str(msg)
            }
            reply = json.dumps({
                'ok': dynamo(result, time),
                'time': time})
            statusCode = 200
    return {
        'statusCode': statusCode,
        'headers': {
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'OPTIONS,POST,GET',
            'Content-Type': 'application/json'
        },
        'body': reply
    }