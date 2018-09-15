from flask import Flask
from flask import request

from twilio.twiml.messaging_response import Body, Message, Redirect, MessagingResponse

app = Flask(__name__)


@app.route("/", methods=['POST'])
def hello():
    print(request.data)
    # parse json to dict
    response = MessagingResponse()
    message = Message()
    message.body("Got the request")
    response.append(message)
    return str(response)