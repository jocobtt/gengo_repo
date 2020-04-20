from flask import Flask 
# add on to this app. Make it do something more stateful - ie take in input and give some output
app = Flask(__name__)

@app.route("/")
def hello():
	return "Hello from Python!"

if __name__ == "__main__":
	app.run(host='0.0.0.0')

