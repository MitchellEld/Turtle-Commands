import subprocess as sp
import os
from flask import Flask, request
from twilio.twiml.messaging_response import Body, Message, MessagingResponse
from command_mapping import command_map, python_command_map
from pathlib import Path

app = Flask(__name__)

verified_numbers = []

# Get the verified numbers are server startup
with open("./setup/verified_numbers", "r") as phone_nums:
    verified_numbers = phone_nums.read().strip('\n')

HOME_PATH = str(Path.home())

@app.route("/", methods=['POST'])
def get_message():
    from_number = request.form['From']
    req_body = request.form['Body']
    response = MessagingResponse()
    message = Message()
    # Verify that phone number is able to make requests
    if from_number not in verified_numbers:
        message.body('You are not authorized')
        response.append(message)
        return str(response)

    # Check first word in body to see if it is custom command
    req_body = req_body.replace('~',HOME_PATH)
    print(req_body)
    bulk_commands = req_body.split(';')
    commands = []
    # new_body = ' ;'.join(bulk_commands)
    for bulk_command in bulk_commands:
        command = bulk_command.split(' ')
        while '' in command:
            command.remove('')
        print(command)
        commands.append(command)
    # If custom command, run function associated with it
    # If not custom command, run the body as normal os command
    output = ''
    for command in commands:
        try:
            if command[0] in command_map:
                pass
            elif command[0] in python_command_map:
                output += python_command_map[command[0]](command[1])
            else:
                output += str(sp.check_output(command),'utf-8')+'\n'
        except:
            output += '{} command failed\n'.format(command[0])

    message.body('Got the request from {}\nCommand output: \n{}'.format(from_number, output))
    response.append(message)
    return str(response)