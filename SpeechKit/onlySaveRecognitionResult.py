# This program only save result of job in file 
import requests
from requests.exceptions import HTTPError
import time
import json

key = '<Your API key>'
id='<ID of operation>'

header = {'Authorization': 'Api-Key {}'.format(key)}


# Request the operation status on the server until recognition is complete.
while True:

    time.sleep(1)

    GET = "https://operation.api.cloud.yandex.net/operations/{id}"
    req = requests.get(GET.format(id=id), headers=header)
    req = req.json()

    if req['done']: break
    print("Not ready")

# Print done if operation done :)
print("Done!")

# Save only text from recognition results.
f = open(id+'.txt','w') 

for chunk in req['response']['chunks']:
    f.write(chunk['alternatives'][0]['text'] + ". ")
f.close()
