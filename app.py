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
		fromPhone= os.environ['FROM_PHONE']
		toPhone= '+17133675645'	# validate phone number using Twilio service?
		messageBody = request.form['message'] + f"- 'Hi {senderName}, Henry can help you send text messages like this one for customer notifications or surveys.' "

		# set message parameters
		message = client.messages \
							.create(
								body=messageBody,
								from_=fromPhone,
								to=toPhone
							)

		# validate and format recipient phone number
		formattedToPhone = client.lookups \
								.phone_numbers(toPhone)
								.fetch(country_code='US')

		print("sent message id:", message.sid)
		print("formatted phone num:", formattedToPhone.phone_number)

	return render_template("index.html")


if __name__=="__main__":
	app.run(debug=True)