from boto3 import resource
from boto3.dynamodb.conditions import Key, Attr
from datetime import datetime
from time import sleep
import random
import requests

def dynamoput(table, record):
    dynamodb = resource('dynamodb')
    table = dynamodb.Table(table)
    try:
        table.put_item(Item=record)
        return f"Submitted"
    except Exception as ex:
        print(ex)
        return f"Error submitting."

def dynamoget(table, sid):
    dynamodb = resource('dynamodb')
    table = dynamodb.Table(table)
    try:
        response = table.query(
            KeyConditionExpression=Key('sid').eq(int(sid))
        )
        return response['Items']
    except Exception as ex:
        print(ex)
        return f'error: cannot get from session id'

def insertradn():
    pass
    #dynamoput('sdd4005', {'sid':834698, 'time':, 'msg':)})

api_url = 'https://6yy8r1njth.execute-api.ap-northeast-1.amazonaws.com/dev'
sid = 834698
name = 'bot01'
for i in range(5):
    ta = datetime.utcnow().strftime("%Y-%m-%d %H-%M-%S")
    sleep(1.5)
    r = requests.get(f'{api_url}/additem?sid={sid}&time={ta}&msg=bot: {hash(ta)}&name={name}')
    results = r.json()
    print(results)
    #insertradn()
"""
que = dynamoget('sdd4005',834698)
for i in que:
    print(('-'*20) + '\n'
f'''Session: {i['sid']}
Time: {i['time']}
Name: {i.get('name', 'noName')}
Message: {i['msg']}''')
"""