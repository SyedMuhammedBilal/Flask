from flask import Flask, render_template
from flask import redirect, jsonify
from flask import url_for, request
from flask_pymongo import PyMongo 

app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb+srv://SyedMuhammed:6cylinder@flask-8touu.mongodb.net/test?retryWrites=true&w=majority"
mongo = PyMongo(app)

@app.route("/")
def index():
	return jsonify({"message": "Hello from 5001", "users": users})

@app.route("/test", methods=["POST"])
def test():
	data = request.form 
	data = dict(data)
	for i, v in enumerate(users):
		if(data["userName"] == v["name"] and data["password"] == v["password"]):
			return redirect("http://127.0.0.1:5000/home")
	return redirect("http://127.0.0.1:5000/login")

if __name__ == '__main__':
	app.run(debug=True)