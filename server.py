from flask import Flask, request
from utils import get_commands, execute_commands

app = Flask(__name__)

@app.route("/", methods=['POST'])
def get_message():
    # from_number = request.form['From']
    req_body = request.form['Body']

    # Check first word in body to see if it is custom command
    commands = get_commands(req_body)
    # If custom command, run function associated with it
    # If not custom command, run the body as normal os command
    output = execute_commands(commands)
    return output
