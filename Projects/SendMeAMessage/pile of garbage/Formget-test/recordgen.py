import requests
import time
API_ENDPOINT = 'https://api.aws.ltek.me'
msg = 'recordgen'
i=0
while True:
    msg = 'recgen'
    r = requests.get(f"{API_ENDPOINT}/form/sumbit?name=recgenmachine&msg={msg+str(i)}")
    print(str(r) + msg)
    i +=1
    time.sleep(1)