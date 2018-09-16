# Turtle-Commands
Project for HowdyHack 2018

---


## Install 
<code>pip install -r requirements.txt</code>

<code>FLASK_APP=server.py flask run</code>

## Slack SETUP
Create a new Slack app: https://api.slack.com/apps?new_app=1 <br/>
Create a name for your app. <br/>
Select or make a new workspace to add the bot to.

From __Basic Information__ get the **Signing Secret**<br/>
From __OAuth & Permissions__ get the **Bot User OAuth Token**

Stick both into the <code>slack.py</code> file to the corresponding variables.

Back to Slack.<br/>
Under __Event Subscriptions__, enable events and put in the server host with the path extension of "/slack/events". Ex: <code>test.com/slack/events</code>
Add the __message.channels__ workspace event to __Event Subscriptions__

## Structure
The __setup__ directory currently contains a file called __verified_numbers__ that should contain the numbers that are allowed to execute commands. Each number should be on a new line. The __setup__ directory also contains an __emails.json__ which should contain a nickname with an associated email for the email custom command.

The __custom-commands__ directory should contain all of the functions for custom commands.

The __command_mapping.py__ file contains a dictionary that should map the custom command name to a function

## Custom Commands
- aggieprint
    - Usage: For setup, use <code>aggieprint set-login \<netid> \<password></code> to login and use your credentials. Then, you can print by <code>aggieprint \<filename></code> and your file will be uploaded to the aggieprint server