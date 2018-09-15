from flask import Flask, request

from twilio.twiml.messaging_response import Body, Message, MessagingResponse

app = Flask(__name__)

verified_numbers = []

with open("./setup/verified_numbers", "r") as phone_nums:
    verified_numbers = phone_nums.readlines()

@app.route("/", methods=['POST'])
def get_message():
    print(request.form['Body'])
    from_number = request.form['From']
    req_body = request.form['Body']
    response = MessagingResponse()
    message = Message()
    # Verify that phone number is able to make requests
    if from_number not in verified_numbers:
        message.body("You are not authorized")
        response.append(message)
        return str(response)

    # Check first word in body to see if it is custom command

    # If custom command, run function associated with it

    # If not custom command, run the body as normal os command

    # Capture output of the command

    # return message with the output
    
    message.body("Got the request")
    response.append(message)
    return str(response)