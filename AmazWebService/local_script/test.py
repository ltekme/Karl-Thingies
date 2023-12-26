from boto3 import resource
from json import dumps
from boto3.dynamodb.conditions import Key

def dynamo(sid):
    dynamodb = resource('dynamodb')
    table = dynamodb.Table('sdd4005')
    try:
        response = table.query(
            KeyConditionExpression=Key('sid').eq(int(sid)),
            ScanIndexForward=False
        )
        items =  response['Items']
        for item in items:
            item['sid'] = int(item['sid'])
        
        return items
    except Exception as ex:
        print(ex)
        return f'error: cannot get from session id'
sid = 834698
items = dynamo(int(sid))
print(dumps(items))