#import requests
import json
from os import path as op

reagon = 'ap-east-1'
service = 'EC2_INSTANCE_CONNECT' # EC2_INSTANCE_CONNECT -> 43.198.192.104/29

#url = 'https://ip-ranges.amazonaws.com/ip-ranges.json'
#ips = requests.get(url).json()

ips = json.load(open(op.join(op.dirname(op.realpath(__file__)), 'ip-ranges.json')))

ips4 = [i for i in ips.get('prefixes') if reagon in i.get('region') and service in i.get('service')]
ips6 = [i for i in ips.get("ipv6_prefixes") if reagon in i.get('region') and service in i.get('service')]

for i in ips4: print(f'{i['service']} -> {i['ip_prefix']}')
for i in ips6: print(f'{i['service']} -> {i["ipv6_prefix"]}')