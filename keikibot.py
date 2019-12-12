import time
import slack  
from slack import RTMClient
OAuth_Access_Token = 'xoxp-858739923331-872067538775-872434335686-9b09de1440262b61e6fd2261263dae10'
Bot_User_OAuth_Access_Token = 'xoxb-858739923331-872085546999-KFHwrbu1sCBOhxVweGNL1JQ0'

# instantiate Slack client
client = slack.WebClient(token = Bot_User_OAuth_Access_Token)


conversations_list = client.conversations_list()['channels']

""" client.chat_postMessage(
    channel = conversations_list[0]['id'],
    text = 'Hello from keikibot'
)

#
members = client.users_list()['members']
print([(member['id'], member['name'], member['is_bot']) for member in members])
for member in members:
    name = member['name']
    if not member['is_bot']:
        conversation_id = client.conversations_open(users=  member['id'])
        #this message comes from slackbot
        client.chat_postMessage( 
            channel = member['id'], #conversation_id['channel']['id'], 
            text = f'Hi to {name}'
        )
        #this message comes from keikibot
        client.chat_postMessage( 
            channel = conversation_id['channel']['id'], 
            text = f':potable_water::potable_water:Hi, {name}! Remember to drink more water today!:potable_water::potable_water:'
        )
 """
@RTMClient.run_on(event="message")
def say_hello(**payload):
  data = payload['data']
  web_client = payload['web_client']

  if 'Thank' in data['text']:
    channel_id = data['channel']
    thread_ts = data['ts']
    user = data['user']

    web_client.chat_postMessage(
      channel=channel_id,
      text=f"You're Welcome <@{user}>! :droplet:",
      thread_ts=thread_ts
    )

rtm_client = RTMClient(token=Bot_User_OAuth_Access_Token)
rtm_client.start()
