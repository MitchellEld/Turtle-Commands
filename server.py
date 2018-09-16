from flask import Flask, request
from utils import get_commands, execute_commands
from slack import responseMessage
import os
from multiprocessing import Process

app = Flask(__name__)

@app.route("/", methods=['POST'])
def get_message():
    # from_number = request.form['From']
    req_body = request.form['Body']
    # Check first word in body to see if it is custom command
    commands = get_commands(req_body)
    # If custom command, run function associated with it
    # If not custom command, run the body as normal os command
    p = Process(target = execute_commands, args = (commands, request.form['Channel']))
    p.start()
    p.join()
    return 'ok'
