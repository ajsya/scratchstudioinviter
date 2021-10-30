import scratchconnect
import json
import requests
import time
import random

login = scratchconnect.ScratchConnect("","")
studio = login.connect_studio(studio_id=30290420)
scratch_studio = 30290420

last_message = None
while True:
    r = requests.get('https://api.scratch.mit.edu/studios/{0}/comments/?limit=40&offset=0'.format(scratch_studio))
    #print(r.content)
    obj = json.loads(r.text)
    #print (json.dumps(obj, indent=2))

    comment_content = obj[0]["content"]
    comment_id1 = obj[0]["id"]
    comment_author = obj[0]["author"]["username"]
    
    keywords = ["invite me", "Invite Me", "invite Me", "Invite me", "iNvItE mE", "InViTe Me", "INVITE ME"]

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

    time.sleep(5) #Increase distance between requests, for testing purposes set at every 5 seconds.
