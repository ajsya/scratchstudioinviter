from scratchclient import ScratchSession

import requests
import json
import time

session = ScratchSession("346383", "iamabot")

studio = 30290420
r = requests.get('https://api.scratch.mit.edu/studios/{0}/comments/?limit=40&offset=0'.format(studio))

print(r.content)
obj = json.loads(r.content)
message = obj[0]['content']
print(message)

last_message = None
while True:
    r = requests.get('https://api.scratch.mit.edu/studios/{0}/comments/?limit=40&offset=0'.format(studio))
    obj = json.loads(r.content)
    message = obj[0]['content']
    author = obj[0]['author']['username']
    
    keywords = ["invite me", "Invite Me", "invite Me", "Invite me", "iNvItE mE", "InViTe Me", "INVITE ME"]

    wants_invited = any(keywords in message for keywords in keywords)
    
    if wants_invited == True:
        if message != last_message:
            print(author)
            session.get_studio(studio).invite_curator(author)
            last_message = message
            print("invited")
        else:
            print("already invited")
    else:
        print("does not want invited")

    time.sleep(5)
