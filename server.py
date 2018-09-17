from flask import Flask, request
from utils import get_commands, execute_commands
from messaging_wrappers.slack import responseMessage
import os
from multiprocessing import Process
from setup.config import FLASK_PORT

app = Flask(__name__)

@app.route("/", methods=['POST'])
def get_message():
    # from_number = request.form['From']
    req_body = request.form['Body']
    print(req_body)
    # Check first word in body to see if it is custom command
    commands = get_commands(req_body)
    # If custom command, run function associated with it
    # If not custom command, run the body as normal os command
    #p = Process(target = execute_commands, args = (commands, request.form['Channel']))
    execute_commands(commands, request.form['Channel'])
    #p.start()
    #p.join()
    return 'ok'

if __name__ == '__main__':
    app.run(port=FLASK_PORT)
