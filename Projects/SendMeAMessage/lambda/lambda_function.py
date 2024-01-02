from datetime import datetime
from boto3 import resource, client
from json import loads, dumps

ses = client('ses', region_name='us-east-1')
tb = resource('dynamodb').Table('SMAM')

def lambda_handler(event, context):
    if event['httpMethod'] == 'POST':
        resault, statusCode = post(event)
    else:
        resault, statusCode = {'ok': 'Hello From SMAM Lambda Function'}, 200
    return {
        'statusCode': statusCode,
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
        },
        'body': dumps(resault)
    }


def post(event):
    if event['path'] == '/sams':
        body = loads(event['body'])
        msg = body['msg']
        if body is None or msg is None or msg == '' or len(msg) >= 200:
            return {'error': 'Invalid Message'}, 400
        else:
            if 'name' not in body or body['name'] is None or body['name'] == '':
                body['name'] = 'Anonmus'
            try:
                print(tb.put_item(Item = {
                    'Time': datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S'),
                    'name': str(body['name']),
                    'msg': msg
                }))
                if eml([body.get('name'),body.get('msg')]):
                    return {'ok': 'Message Sent'}, 200
                else:
                    return {'ok': 'Message Saved'}, 200
            except Exception:
                return {'error': 'Something Went Wrong'}, 500
    else:
        return {'error': 'Empty'}, 400


def eml(content) -> bool:
    data = f"""<html>
        <head></head>
        <body>
          <h2>New Message!</h2>
          <p>From: {content[0]}</p>
          <p>Message: {content[1]}</p>
        </body>
        </html>"""
    try:
        print(ses.send_email(
            Destination={'ToAddresses': ['karl@ltek.me']},
            Source= 'smam@aws.ltek.me',
            Message={
                'Body': {
                    'Html': {
                        'Charset': 'UTF-8',
                        'Data': data,
                    }
                },
                'Subject': {
                    'Charset': 'UTF-8',
                    'Data': 'New Message!',
                },
            }
        ))
        return True
    except Exception as ex:
        print(f"Error: {ex}")
        return False