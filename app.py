from flask import Flask, request, render_template
from twilio.rest import Client
import os

app = Flask(__name__)	# creates instance of Flask app and exports app so can be used as module or package

@app.route('/', methods=["GET", "POST"])
def send_sms():

	if request.method == "POST":
		# instantiate Client object
		account_sid = os.environ['TWILIO_ACCOUNT_SID']#'AC872e613bcaf8a610ce583aee6a6ce844'	
		auth_token = os.environ['TWILIO_AUTH_TOKEN']#'ad657ad8d45e0a9490666a14fdf2ef6a'	
		client = Client(account_sid, auth_token)

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
		print("sent message?", message.sid)

	return render_template("index.html")

# @app.route("/form-test", methods=["GET", "POST"])
# def index():
	
# 	if request.method == "POST":
		
# 		# TASK: validate phone number works with Twilio API

# 		#name = request.form["name"]
# 		targetPhone = request.form["recipient-phone"]	
# 		messageBody = request.form["message"]
		
# 		# print ("user's name:", name)
# 		print("targetPhone value:", targetPhone)
# 		print("messageBody value:", messageBody)

# 		#TASK: try/catch errors?
		
# 	return render_template("index.html")


if __name__=="__main__":
	app.run(debug=True)