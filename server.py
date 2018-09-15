from flask import Flask, request

from twilio.twiml.messaging_response import Body, Message, MessagingResponse

app = Flask(__name__)

@app.route("/", methods=['POST'])
def get_message():
    print(request.form['Body'])
    # parse json to dict
    response = MessagingResponse()
    message = Message()
    message.body("Got the request")
    response.append(message)
    return str(response)