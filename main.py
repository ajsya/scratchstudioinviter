import scratchconnect
import json
import requests
import time
import random
import os
from dotenv import load_dotenv

load_dotenv()

username = os.environ['USERNAME']
password = os.environ['PASSWORD']
scratch_studio = os.environ['STUDIO_ID']

login = scratchconnect.ScratchConnect(username, password)
studio = login.connect_studio(studio_id=scratch_studio)

last_message = None
while True:
    r = requests.get('https://api.scratch.mit.edu/studios/{0}/comments/?limit=40&offset=0'.format(scratch_studio))
    #print(r.content)
    obj = json.loads(r.text)
    #print (json.dumps(obj, indent=2))

    comment_content = obj[0]["content"]
    comment_id1 = obj[0]["id"]
    comment_author = obj[0]["author"]["username"]
    
    keywords = ["invite me", "Invite Me", "invite Me", "Invite me", "iNvItE mE", "InViTe Me", "INVITE ME", "can I join", "Can I join", "CAN I JOIN", "can I curate", "Can I curate", "CAN I CURATE", "can I be a curator", "Can I be a curator", "CAN I BE A CURATOR", "ADD ME", "add me", "Add me", "Add Me"]

    wants_invited = any(keywords in comment_content for keywords in keywords)
    
    if wants_invited == True:
        if comment_content != last_message:
            print(comment_author, " wants invited.")
            studio.invite_curator(comment_author)
            last_message = comment_content
            studio.reply_comment(content="Invited! Welcome to {0}, {1}! ({2})".format(studio.title(), comment_author, random.randint(100, 100000)), comment_id=comment_id1)
            print(comment_author, " successfully invited! :)")
        else:
            print("User has been already invited.")
    else:
        print("Author of latest comment does not want to be invited.")

    time.sleep(18000) #Increase distance between requests, for testing purposes set at every 5 seconds.
