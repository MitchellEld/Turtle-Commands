import subprocess as sp
from flask import Flask, request
from twilio.twiml.messaging_response import Body, Message, MessagingResponse
from command_mapping import command_map

app = Flask(__name__)

verified_numbers = []

with open("./setup/verified_numbers", "r") as phone_nums:
    verified_numbers = phone_nums.read().strip('\n')

@app.route("/", methods=['POST'])
def get_message():
    print(request.form['Body'])
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
    bulk_commands = req_body.split(';')
    new_body = ' ;'.join(bulk_commands)
    command = new_body.split(' ')
    if '' in command:
        command.remove('')
    print(command)
    # If custom command, run function associated with it
    # If not custom command, run the body as normal os command
    output = ''
    try:
        if command[0] in command_map:
            pass
        else:
            output = str(sp.check_output(command),'utf-8')
    except:
        output = '{} command failed'.format(command[0])

    message.body('Got the request from {}\nCommand output: \n{}'.format(from_number, output))
    response.append(message)
    return str(response)