
import boto3
def saves3(cent, time):
    s3 =  boto3.client("s3")
    bukkit = 'formd-records'
    file = time + '.txt'
    try:
        content = "\n".join(cent)
        s3.put_object(Body=content, Bucket=bukkit, Key=file)
        return f"message saved to s3 as {time}"
    except Exception as e:
        return  f"oops... s3 error"

def dynamo(cent, time):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('FormProdMessages')
    try:
        table.put_item(Item={
        'datetime': time,
        'Name': str(cent[0]),
        'Message': str(cent[1]),
        'contact': str(cent[2])
        })
        return f"Your message is saved to dynamo. Thank You."
    except Exception as ex:
        return f"oops... error saving message to dynamoDB."