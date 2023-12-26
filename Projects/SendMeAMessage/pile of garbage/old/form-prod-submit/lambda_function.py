import pystache
from datetime import datetime
import saver


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
        
def lambda_handler(event, context):
    time = datetime.utcnow()
    name, message, contact, return_msg = "", "", "", ""
    query_params = event['queryStringParameters']
    if query_params:
        name = query_params.get('name')#, 'noName'
        message = query_params.get('msg')#, 'noMessage'
        contact = query_params.get('contact')#, 'noContact
    else:
        return_msg = "Empty. Why?"
    if message == '' and name == '' and contact == '':
        return_msg = "Empty. Why?"
    elif len(message) >= 500:
        return_msg = "Very nice, I'm pretty sure you wrote a beautiful message. Thank you, but it is way too long. Try sending in segments? There is a conact field, maybe your email? I like to chat with people"
    elif len(name) >= 100:
            return_msg = "Please. A name I can use to address you. You are 100% not the loard with a 737 charactor long name. Pretty sure you have a beautiful name, but it's way too long for me"
    elif len(contact) >= 100:
        return_msg = 'Please. Ony way for me to reach you. This is way too long. Phone? Email? Insta? Thank you.'
    else:
        return_msg = saver.dynamo( [name, message, contact], str(time.strftime("%Y%m%d%H%M%S%f")))#saves3(user_record ,str(time.strftime("%Y%m%d_%H-%M-%S-%f"))),
    data={
        "resault": return_msg,
        "name": name,
        "contact": contact,
        "Message": message,
        "time": str(time.strftime("%Y-%m-%d %H:%M:%S"))
    }
    template = open('template.html').read()
    resault = pystache.render(template, data)
    return {
        'statusCode': 200,        
        'headers': {'Content-Type': 'text/html'},
        'body': resault
    }