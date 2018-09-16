# Turtle-Commands
Project for HowdyHack 2018

---


## Install 
<code>pip install -r requirements.txt</code>

<code>FLASK_APP=server.py flask run</code>

## Structure
The __setup__ directory currently contains a file called __verified_numbers__ that should contain the numbers that are allowed to execute commands. Each number should be on a new line. The __setup__ directory also contains an __emails.json__ which should contain a nickname with an associated email for the email custom command.

The __custom-commands__ directory should contain all of the functions for custom commands.

The __command_mapping.py__ file contains a dictionary that should map the custom command name to a function

## Custom Commands
- aggieprint
    - Usage: For setup, use <code>aggieprint set-login \<netid> \<password></code> to login and use your credentials. Then, you can print by <code>aggieprint \<filename></code> and your file will be uploaded to the aggieprint server