import zipfile
import boto3
from os import path as op, environ

from dotenv import load_dotenv

load_dotenv()

zip_file = op.join(op.dirname(op.realpath(__file__)),'function.zip')
archive = zipfile.ZipFile(zip_file, 'w')
zip.write('index.js', 'path/on/disk/index.js')

def create_function(function_name, region, bucket, akey, skey):
    s3_client = boto3.client(region)
    s3_client.put_object(Body=archive, Bucket=bucket, Key='function.zip')

    lambda_Client = boto3.client('lambda', aws_access_key_id=akey,
                       aws_secret_access_key=skey,region_name=region)
    
    response = lambda_Client.create_function(
            Code={
                'S3Bucket': bucket,
                'S3Key': 'function.zip',
            },
            Description='Process image objects from Amazon S3.',
            FunctionName=function_name,
            Handler='index.handler',
            Publish=True,
            Role='arn:aws:iam::123456789012:role/lambda-role',
            Runtime='nodejs12.x',
        )
    return response