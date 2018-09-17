# Turtle Commands
Project started at HowdyHack 2018 by Thomas McDonald, Nicko Enochs, Mitchell Eldridge, and Alejandro Londono

---
## Running
NOTE: Configured Flask port in <code>setup/config.py</code> will run with the single script below
### Individual commands
<code>pip install -r requirements.txt</code>

<code>FLASK_APP=server.py flask run --port=<PORT#></code>

<code>python slack.py</code>

### Single script
<code>python run.py</code>

## Slack SETUP
Create a new Slack app: https://api.slack.com/apps?new_app=1 <br/>
Create a name for your app. <br/>
Select or make a new workspace to add the bot to.

From __Basic Information__ get the **Signing Secret**<br/>
In __Bot Users__ create a bot user <br/>
In __OAuth & Permissions__ add the bot to workspace
From __OAuth & Permissions__ get the **Bot User OAuth Token**

Stick both the **Signing Secret** and the **Bot User OAuth Token** into the <code>setup/config.py</code> file to the corresponding variables.

Back to Slack.<br/>
Under __Event Subscriptions__, enable events and put in the server host with the path extension of "/slack/events". Ex: <code>test.com/slack/events</code>
Add the __message.channels__ workspace event to __Event Subscriptions__<br/>
Then, add __message.channels__ as a Bot User Event

NOTE: Make sure to run both the flask server and slack.py

FOR DEVELOPMENT: You can use ngrok as a tool to tunnal traffic to your machine

## Structure
The __setup__ directory currently contains a file called __verified_numbers__ that should contain the numbers that are allowed to execute commands. Each number should be on a new line. The __setup__ directory also contains an __emails.json__ which should contain a nickname with an associated email for the email custom command.

The __custom-commands__ directory should contain all of the functions for custom commands.

The __command_mapping.py__ file contains a dictionary that should map the custom command name to a function. All functions used in the <code>command_map</code> dictionary must take one input (whether it is used or not), which is a list of strings. The function must also return a string which can be an empty string. <br/>
All functions used in the <code>python_command_map</code> must have one input which is a plain string and does not need an output (it will not be used, even if provided).

The __messaging_wrappers__ directory contain "wrappers" for any kind of service that you would like to connect to have this functionality. These wrappers are essentially other services running that take a request from the specific service (i.e. Slack) get the text body and make a request to the Flask server that executes the commands. Currently, the only wrapper is the <code>slack.py</code> (Slack) wrapper for connecting a Slack bot to the service. Other wrappers that can be added are Twilio (for SMS), Discord, etc.

## Custom Commands
- aggieprint (For Texas A&M University students)
    - Usage: For setup, use <code>aggieprint set-login \<netid> \<password></code> to login and use your credentials. Then, you can print by <code>aggieprint \<filename></code> and your file will be uploaded to the aggieprint server

## Currently used ports
These ports can be modified in the <code>setup/config.py</code>
- Slack: 3000
- Flask (Main service): 5000