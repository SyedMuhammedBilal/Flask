from flask import Flask, request
from flask import redirect, url_for
from flask import jsonify
from flask_pymongo import PyMongo 

app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb+srv://SyedMuhammed:6cylinder@flask-8touu.mongodb.net/test?retryWrites=true&w=majority"
mongo = PyMongo(app)
print(mongo)

@app.route("/")
def index():
	usersData = mongo.db.usersData
	data = usersData.find({},{"password": 0, "_id": 0})
	data1 = []
	for i in data:
		#i["_id"] = str(i["_id"])
		data1.append(i)
	print(data1)
	return jsonify({"msg": "Hello PostMan", "data": data1})

@app.route("/findEmail", methods=["POST"])
def findEmail():
	data = dict(request.form)
	usersData = mongo.db.usersData
	data = usersData.find({"userName": data["userName"] },{"password": 0, "_id": 0})
	data1 = []
	for i in data:
		data1.append(i)
	return jsonify({"data": data1})

@app.route("/findUserName/<userName>")
def findUserName(userName):
	usersData = mongo.db.usersData
	data = usersData.find({"userName": userName },{'password': 0, '_id': 0})
	for i in data:
		data1.append(i)
	return jsonify({"data": data1})

if __name__ == '__main__':
	app.run(debug=True)