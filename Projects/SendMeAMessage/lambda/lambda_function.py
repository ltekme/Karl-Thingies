import json
import boto3
from datetime import datetime


def dynamo(record, time):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('FormMessages')
    sumbitDate = time.strftime('%Y-%m-%d')
    clock = time.strftime('%H%M%S') + time.strftime('%f')[:2]
    record['submitDate'] = str(sumbitDate)
    record['submitTime'] = str(clock)
    try:
        table.put_item(Item=record)
        return f"Your message is saved to dynamo. Thank You."
    except Exception as ex:
        return f"oops... error saving message to dynamoDB. {ex}"


def lambda_handler(event, context):
    body, record, respones, headers={}, {}, {}, {}
    headers = {
        'Content-Type': 'application/json',
        'Access-Control-Allow-Origin': '*'
    }
    time = datetime.utcnow()

    #assume empty
    statusCode = 403
    body['oops...'] = 'Incomplete request'
    message,name = '',''


    query_params = event.get('queryStringParameters', None)
    if query_params is None:
        statusCode = 400
        body = {'error': 'Missing Param'}

    elif query_params.get('msg') == '':
        statusCode = 400
        body = {'oops...': 'Missing Message'}

    else: 
        name = query_params.get('name', 'noName')
        message = query_params.get('msg')

        record = {
            'Name': name,
            'Messages': message
        }

        # respones Body
        body = {
            'ok': str(dynamo(record, time)),
            'name': name,
            'message': message,
            'time': str(time.strftime('%Y-%m-%d %H:%M:%S'))
        }
        statusCode = 200
    
    respones = {
        'statusCode': statusCode,
        'headers': headers,#{'Content-Type': 'application/json'},
        'body': json.dumps(body)
    }
    
    return respones