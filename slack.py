from slackeventsapi import SlackEventAdapter
from slackclient import SlackClient
import os
import requests


url = "http://127.0.0.1:5000"

# Our app's Slack Event Adapter for receiving actions via the Events API
slack_signing_secret = 'da82529a03ba7e478e3ee2770bfa7dce'
slack_events_adapter = SlackEventAdapter(slack_signing_secret, "/slack/events")

slack_client = SlackClient('xoxb-435732900096-436461570514-afavU32dRQt8aT98iSP2HPQj')

@slack_events_adapter.on("message")
def handle_message(event_data):
    #print(event_data)
    if "user" in event_data["event"]:
        r = requests.post(url, data = {'Body': event_data['event']['text'], 'Channel': event_data['event']['channel']})
        slack_client.api_call("chat.postMessage", channel=event_data['event']["channel"], text=r.text)

def responseMessage(responseContent, respChannel):
    slack_client.api_call("chat.postMessage", channel=respChannel, text=responseContent)

slack_events_adapter.start(port=3000)
