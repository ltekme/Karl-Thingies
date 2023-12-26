import boto3
import glob
import os
import zipfile
import requests
import sys
import json
import tempfile


def lambda_update():
    print('update function code')
    buckit = 'lambdafunc-hk'
    region_name = 'ap-east-1'
    zipfn = 'lambda_code_iwrp.zip'
    with zipfile.ZipFile(zipfn, "w") as z:
        for fl in  glob.glob('lambda/*'):
            d, f = os.path.split(fl)
            z.write(fl, f)

    # upload file
    function_name = 'iwrp-rw'
    s3_client = boto3.client('s3', region_name=region_name)
    s3_client.upload_file(zipfn, buckit, zipfn)

    # update function code
    lambda_client = boto3.client('lambda',region_name=region_name)
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


args = sys.argv[1:]
if '-u' in args:
    try:
        lambda_update()
    except Exception as ex:
        print(f'cannot update\n{ex}')
if '-d' in args:
    url = f'https://7yll41tdl8.execute-api.ap-east-1.amazonaws.com/prod/iwrp-func/debug{args[1]}'
    with open('mock.json', 'w') as mockjson:
        json.dump(requests.get(url).json(), mockjson, indent=4)
if '-t' in args:
    url = [
        'https://7yll41tdl8.execute-api.ap-east-1.amazonaws.com/prod/iwrp-func/post?sid=718172&name=&msg=abcd',
        'https://7yll41tdl8.execute-api.ap-east-1.amazonaws.com/prod/iwrp-func/view?sid=718172',
    ]
    for c, i in enumerate(url): 
        print(f'REQ_{c}: {requests.get(i).json()}')
if '-fuck' in args:
    print(requests.get('https://7yll41tdl8.execute-api.ap-east-1.amazonaws.com/prod/iwrp-func/post').headers)
    print(requests.get('https://oviwomsjf6.execute-api.ap-northeast-1.amazonaws.com/dev/Messages/Submit').headers)