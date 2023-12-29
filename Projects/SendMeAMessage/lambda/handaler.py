from datetime import datetime
from boto3 import resource
from json import loads

tb = resource('dynamodb').Table('SMAM')

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
                tb.put_item(Item = {
                    'Time': datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S'),
                    'name': str(body['name']),
                    'msg': msg
                })
                return {'ok': 'Message Sent'}, 200
            except Exception:
                return {'error': 'Something Went Wrong'}, 500
    else:
        return {'error': 'Empty'}, 400
