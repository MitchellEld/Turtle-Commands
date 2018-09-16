from slackeventsapi import SlackEventAdapter
from slackclient import SlackClient
import os
import requests


url = "http://127.0.0.1:5000"

# Our app's Slack Event Adapter for receiving actions via the Events API
slack_signing_secret = 'ee27682f369686232b096439eecdb8a2'
slack_bot_user_oauth_token = 'xoxb-436597440994-437950307830-bsuElvUuyzr5yO3sMJMCVu98'

slack_events_adapter = SlackEventAdapter(slack_signing_secret, "/slack/events")

slack_client = SlackClient(slack_bot_user_oauth_token)

@slack_events_adapter.on("message")
def handle_message(event_data):
    if "user" in event_data["event"]:
        r = requests.post(url, data = {'Body': event_data['event']['text'], 'Channel': event_data['event']['channel']})

def responseMessage(responseContent, respChannel):
    slack_client.api_call("chat.postMessage", channel=respChannel, text=responseContent)

slack_events_adapter.start(port=3000)
