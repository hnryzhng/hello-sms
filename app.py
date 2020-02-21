from flask import Flask, request, render_template
from twilio.rest import Client
import os

# instantiate and export Flask app
app = Flask(__name__)

# instantiate Twilio client
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)

# routes
@app.route('/', methods=["GET", "POST"])
def send_sms():

	if request.method == "POST":

		# TASK: limit two successful messages per IP address (to account for recipient phone num input error)
		# TASK: validate recipient phone number

		# message parameters
		senderName = request.form['sender-name']
		fromPhone='+12562570087'
		toPhone= '+17133675645'	# request.form['recipient-phone']	# validate phone number using Twilio service?
		messageBody = request.form['message'] + f"- 'Hi {senderName}, Henry can help you send text messages like this one for customer notifications or surveys.' "

		# set message parameters
		message = client.messages \
							.create(
								body=messageBody,
								from_=fromPhone,
								to=toPhone
							)
		print("sent message id:", message.sid)

	return render_template("index.html")


if __name__=="__main__":
	app.run(debug=True)