import flask
from flask import request, jsonify

app = flask.Flask(__name__)

@app.route('/greet', methods=['GET'])
def home():
	
	if 'name' in request.args:
		name = str(request.args['name'])
		return "Welcome to docker training - " + name
	else:
		return "Error: No name field provided. Please specify an name (/greet?name=myname)."

if __name__ == "__main__": 
    app.run(host ='0.0.0.0', port = 5001, debug = True)  