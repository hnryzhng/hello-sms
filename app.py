from flask import Flask, request, render_template, jsonify
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
		toPhone= '713 367 5645'	# validate phone number using Twilio service?
		messageBody = request.form['message'] + f"- 'Hi {senderName}, Henry can help you send text messages like this one for customer notifications or surveys.' "

		# validate and format recipient phone number
		outputToPhone = client.lookups \
								.phone_numbers(toPhone)	\
								.fetch(country_code='US')

		formattedToPhone = outputToPhone.phone_number


		# TASK: set message parameters if recipient phone number exists
		# how to get the response status code from outputToPhone?
		
		message = client.messages \
							.create(
								body=messageBody,
								from_=fromPhone,
								to=formattedToPhone
							)


		print("sent message id:", message.sid)
		print("formatted phone num:", formattedToPhone)

	
	return render_template("index.html")



if __name__=="__main__":
	app.run(debug=True)