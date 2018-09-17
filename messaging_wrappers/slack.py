from slackeventsapi import SlackEventAdapter
from slackclient import SlackClient
import os
import requests
import sys
# Update Python path to see root directory for imports
filepath = os.path.dirname(os.path.abspath(__file__)).replace('/messaging_wrappers','')
sys.path.insert(0, filepath)
from setup.config import slack_bot_user_oauth_token, slack_signing_secret, FLASK_PORT, SLACK_PORT


url = "http://127.0.0.1:{}".format(FLASK_PORT)


slack_events_adapter = SlackEventAdapter(slack_signing_secret, "/slack/events")

slack_client = SlackClient(slack_bot_user_oauth_token)

@slack_events_adapter.on("message")
def handle_message(event_data):
    if "user" in event_data["event"]:
        r = requests.post(url, data = {'Body': event_data['event']['text'], 'Channel': event_data['event']['channel']})

def responseMessage(responseContent, respChannel):
    slack_client.api_call("chat.postMessage", channel=respChannel, text=responseContent)

slack_events_adapter.start(port=SLACK_PORT)
