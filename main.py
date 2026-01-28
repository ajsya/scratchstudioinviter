import time, random, os
from dotenv import load_dotenv
import scratchattach as sa

load_dotenv()

session = sa.login(os.environ['USERNAME'], os.environ['PASSWORD'])
studio = session.connect_studio(os.environ['STUDIO_ID'])

keywords = [
    "invite me", 
    "Invite Me", 
    "invite Me", 
    "Invite me", 
    "iNvItE mE", 
    "InViTe Me", 
    "INVITE ME", 
    "can I join", 
    "Can I join", 
    "CAN I JOIN", 
    "can I curate", 
    "Can I curate", 
    "CAN I CURATE", 
    "can I be a curator", 
    "Can I be a curator", 
    "CAN I BE A CURATOR", 
    "ADD ME", 
    "add me", 
    "Add me", 
    "Add Me", 
    "invited", 
    "invite", 
    "Invite", 
    "join", 
    "JOIN", 
    "may I join?", 
    "May I join?", 
    "MAY I JOIN?", 
    "please add me", 
    "Please add me", 
    "PLEASE ADD ME", 
    "i would like to join", 
    "I would like to join", 
    "I WOULD LIKE TO JOIN",
    "Can I be curator",
    "curator",
    "Curator",
    "CURATOR",
    "curate",
    "Curate",
    "CURATE"
]

responses = [
    "I sent you an invite.",
    "You’ve been invited.",
    "Invite sent.",
    "Just invited you.",
    "I added you.",
    "Sent you an invite.",
    "I invited you to join.",
    "You should see an invite from me.",
    "I sent the invite just now.",
    "Invite should be there now.",
    "I added you to it.",
    "I’ve sent you an invitation.",
    "You’re invited, feel free to join.",
    "I went ahead and invited you.",
    "I added you as a member.",
    "Just sent you an invite.",
    "You should have an invite now.",
    "The invite has been sent.",
    "I added you so you can check it out.",
    "I invited you to be part of it.",
    "You’re invited.",
    "I sent one your way.",
    "You should see it in your messages.",
    "Invite sent, let me know if you don’t see it."
]

starting_offset = 85
i = 0
while i < 50:
    print(i)

    comments = studio.comments(limit=40, offset=starting_offset + (i * 40))
    print(comments)

    h = 0
    for comment in comments:
        print(i, h)
        comment_content = comment.content
        comment_id = comment.id
        comment_author = comment.author_name
        data_created = comment.datetime_created
        print(comment_content, comment_id, comment_author, data_created)

        wants_invited = any(keywords in comment_content for keywords in keywords)

        if wants_invited:
            print(f"{comment_author} wants invited.")
            try:
                studio.invite_curator(comment_author)
                print(f"{comment_author} successfully invited! :)")
                try:
                    reply = random.choice(responses)
                    studio.reply_comment(
                        f"{reply} Welcome to {studio.title}, {comment_author}! ({random.randint(100, 100000)})",
                        parent_id=comment_id
                    )
                    print(f"Replied to {comment_author}'s comment.")
                    time.sleep(31)  # Sleep to avoid hitting rate limits
                except Exception as e:
                    print(f"Failed to reply to {comment_author}'s comment: {e}")
            except Exception as e:
                print(f"Failed to invite {comment_author}: {e}")
        else:
            print(f"{comment_author} does not want invited.")
        h += 1

    i += 1