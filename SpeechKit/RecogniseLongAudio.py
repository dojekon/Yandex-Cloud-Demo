import requests
from requests.exceptions import HTTPError
import time
import json

key = '<Your API key>'
filelink='<URI to file in Yandex Object Storage (bucket)>'
POST = "https://transcribe.api.cloud.yandex.net/speech/stt/v2/longRunningRecognize"

# JSON for Russian language and 16kHZ stereo WAW file
body ={
    "config": {
        "specification": {
            "languageCode": "ru-RU",
            "audioEncoding": "LINEAR16_PCM",
            "sampleRateHertz": 16000,
            "audioChannelCount": 2
        }
    },
    "audio": {
        "uri": filelink
    }
}

header = {'Authorization': 'Api-Key {}'.format(key)}

req = requests.post(POST, headers=header, json=body)
data = req.json()
print(data)

id = data['id']

# Request the operation status on the server until recognition is complete.
while True:

    time.sleep(1)

    GET = "https://operation.api.cloud.yandex.net/operations/{id}"
    req = requests.get(GET.format(id=id), headers=header)
    req = req.json()

    if req['done']: break
    print("Not ready")

# Show the full server response in JSON format.
print("Done!")

# Output only text from recognition results
f = open(id+'.txt','w') 

for chunk in req['response']['chunks']:
    f.write(chunk['alternatives'][0]['text'] + ". ")
f.close()
