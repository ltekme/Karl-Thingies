import boto3
from glob import glob
from os import path as op
from zipfile import ZipFile
import requests
import sys
import json

cdir = op.dirname(op.realpath(__file__))

def lambda_update():
    print('update function code')
    
    function_name = 'smam'
    buckit = 'lambdafunc-hk'
    region_name = 'ap-east-1'

    # zpi file
    zipfn =  f'lambda-{function_name}.zip'
    zipfnfile = op.join(cdir, zipfn)
    with ZipFile(zipfnfile, "w") as zip:
        for file in glob('lambda/*'):
            zip.write(file, op.basename(file))

    # upload file
    s3_client = boto3.client('s3', region_name=region_name)
    s3_client.upload_file(zipfnfile, buckit, zipfn)

    # update function code
    lambda_client = boto3.client('lambda', region_name=region_name)
    function = lambda_client.get_function(FunctionName=function_name)
    status = function['Configuration']['LastUpdateStatus']
    print(f'Function Last Update Status: {status}')
    if status == 'InProgress':
        print('Function Updating')
    else:
        lambda_client.update_function_code(
            FunctionName=function_name,
            S3Bucket=buckit,
            S3Key=zipfn,
            Publish=True
        )
        lambda_client.get_waiter('function_updated').wait(FunctionName=function_name)
        print('Function Finish Updating')


url = 'https://7yll41tdl8.execute-api.ap-east-1.amazonaws.com/prod/sams'
name = 'smam'
args = sys.argv[1:]

if '-u' in args:
    try:
        lambda_update()
    except Exception as ex:
        print(f'cannot update\n{ex}')

if '-d' in args:
    durl = f'{url}/debug'
    with open(op.join(cdir, 'mock_p.json'), 'w') as mockjson:
        response = requests.post(
                durl, 
                json = {"somekey": "somevalue"}
            ).json()
        json.dump(response, mockjson, indent=4)

if '-t' in args:
    print(f'GET: {requests.get(url).json()}')
    content = {
        'msg': 'test message'
    }
    print(f'POST: {requests.post(url, json = content).json()}')
    
if '-fuck' in args:
    print(requests.get(f'{url}').headers)