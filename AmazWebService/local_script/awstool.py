import boto3
from boto3.dynamodb.conditions import Key , Attr
def create_dynamo_table(table_name, pk):
    DDB = boto3.resource('dynamodb', region_name='ap-east-1')
    
    params = {
        'TableName': table_name,
        'KeySchema': [
            {'AttributeName': pk, 'KeyType': 'HASH'}
        ],
        'AttributeDefinitions': [
            {'AttributeName': pk, 'AttributeType': 'S'}
        ],
        'ProvisionedThroughput': {
            'ReadCapacityUnits': 1,
            'WriteCapacityUnits': 1
        }
    }
    table = DDB.create_table(**params)
    table.wait_until_exists()
    ret = f'{table.table_arn} Created'
    print(ret)
    return ret
#create_dynamo_table('SMAM', 'Time')
def get_dynamo_arn(t_name):
    arn = boto3.resource('dynamodb').Table(t_name).table_arn
    print(arn)
    return arn

def dynamo_put(table, record):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(table)
    try:
        table.put_item(Item=record)
        return f"Record  inserted into table"
    except Exception as ex:
        print(ex)
        return f"Error submitting."

def dynamoget(table, sid):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(table)
    try:
        response = table.query(
            KeyConditionExpression=Key('sid').eq(int(sid)),
            ScanIndexForward=False
        )
        return response['Items']
    except Exception as ex:
        print(ex)
        return f'error: cannot get from session id'