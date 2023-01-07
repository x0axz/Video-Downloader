import re
import requests
import json

videoLink = input("Enter Loom Video URL: ")

linkList = re.split("/", videoLink)

videoId = linkList[-1]

transcodedURL = "https://www.loom.com/api/campaigns/sessions/" + \
    videoId + "/transcoded-url"

postRequest = requests.post(transcodedURL)

deserialize = json.loads(postRequest.text)

videoURL = deserialize['url']

print("Downloading...")

downloadVideo = requests.get(videoURL)

f = open(videoId + ".mp4", 'wb')
for chunk in downloadVideo.iter_content(chunk_size=255):
    if chunk:
        f.write(chunk)

f.close()

print("Done!")
