from flask import Flask, request

from twilio.twiml.messaging_response import Body, Message, MessagingResponse

app = Flask(__name__)

@app.route("/", methods=['POST'])
def get_message():
    print(request.form['Body'])
    # Verify that phone number is able to make requests

    # Check first word in body to see if it is custom command

    # If custom command, run function associated with it

    # If not custom command, run the body as normal os command

    # Capture output of the command

    # return message with the output
    response = MessagingResponse()
    message = Message()
    message.body("Got the request")
    response.append(message)
    return str(response)