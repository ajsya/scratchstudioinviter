# WORKING! :)
# https://github.com/CubeyTheCube/scratchclient

from scratchclient import ScratchSession
import requests
import json

# https://api.scratch.mit.edu/studios/30290420/comments/?limit=40&offset=0

session = ScratchSession("346383", "iamabot")

# post comments
session.get_user("ajsya_test").post_comment("uwu ami")

# studioComment = session.get_studio(30290420).post_comment('owo scratch studios')
session.get_studio(30290420).invite_curator('ajsya_test') #Invite user to studio

studio = 30290420
r = requests.get('https://api.scratch.mit.edu/studios/{0}/comments/?limit=40&offset=0'.format(studio))

print(r.content)
obj = json.loads(r.content)
message = obj[0]['content']
# print(obj[0]["content"])
print(message)
