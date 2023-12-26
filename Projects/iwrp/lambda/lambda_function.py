import json
from boto3 import resource
from boto3.dynamodb.conditions import Key
from datetime import datetime as dt, timedelta as td

table = resource('dynamodb').Table('iwrp-prod')
error_msg = [{'error':'Invalid API Call'},
             {'error': 'Something went wrong'}]


def lambda_handler(event, context):

    if event["path"] == "/iwrp-func/post":
        if event["httpMethod"] == "POST":
            pass#returs, statusCode = post(event)
        returs, statusCode = post(event)

    elif event["path"] == "/iwrp-func/view":
         returs, statusCode = view(event)

    elif event["path"] == "/iwrp-func/debug":
         returs, statusCode = event, 200

    else:
         returs, statusCode = f'Hello From iwrp Lambda Function', 200

    return {
        'statusCode': statusCode,
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
        },
        'body': json.dumps(returs)
    }


def testc(q) -> bool:
    if q is None or q['sid'] is None or q['sid'] == '':
        return False
    else:
        return True
    
def post(event):
    time = dt.utcnow()
    query_params = event["queryStringParameters"]
    if testc(query_params) and 'msg' in query_params:
        sid = query_params['sid']
        msg = query_params['msg'] 
        name = query_params['name'] or '--'
        if msg is None or msg == '' or len(msg) >= 128:
            return {'error': 'Invalid Response'}, 400
        else:
            try:
                table.put_item(Item=
                    {'sid': str(sid),
                    'time': time.strftime('%Y-%m-%d %H-%M-%S'),
                    'name': str(name),
                    'msg': str(msg),
                    'TTL': int((time + td(hours=1)).timestamp())}
                )
                return {'ok': 'Your Response Has Been Submited'}, 200
            except Exception as ex:
                print(f"Function Error(post): {ex}")
                return error_msg[1] , 500
    else:
        return error_msg[0], 400

def view(event):
    query_params = event["queryStringParameters"]
    if testc(query_params):
        sid = query_params['sid']
        try:
            response, items = table.query(
                KeyConditionExpression=Key('sid').eq(str(sid)),
                ScanIndexForward=False
            ), []
            for i in response['Items']:
                items.append(
                    {'time': i['time'] or '',
                    'name': i['name'] or '',
                    'msg': i['msg'] or ''}
                )
            return items, 200
        except Exception as ex:
            print(f"Function Error(view): {ex}")
            return error_msg[1] , 500
    else:
        return error_msg[0], 400