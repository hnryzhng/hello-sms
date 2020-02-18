from flask import Flask, request, render_template
app = Flask(__name__)	# creates instance of Flask app and exports app so can be used as module or package

@app.route("/", methods=["GET", "POST"])
def index():
	
	if request.method == "POST":
		
		# TASK: validate phone number works with Twilio API

		recipientPhone = request.form["recipient-phone"]	
		sendMessage = request.form["message"]
		print("recipientPhone value:", recipientPhone)
		print("sendmessage value:", sendMessage)

		#TASK: try/catch errors?
		
	return render_template("index.html")

if __name__=="__main__":
	app.run(debug=True)