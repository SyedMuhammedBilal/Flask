from datetime      import datetime
from flask         import Flask, render_template
from flask         import redirect, request
from flask         import url_for
from flask_pymongo import PyMongo
import bcrypt
from flask         import jsonify

app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb+srv://SyedMuhammed:6cylinder@flask-8touu.mongodb.net/test?retryWrites=true&w=majority"
mongo = PyMongo(app)

@app.route("/")
def index():
	return render_template("index.html")

# -------------------------------------------------------------------------------------------------------------#

@app.route("/home")
def home():
	return render_template("home.html")

# -------------------------------------------------------------------------------------------------------------#

@app.route("/signup")
def signin():
	return render_template("signin.html")

# -------------------------------------------------------------------------------------------------------------#

@app.route("/signupAuth", methods=["POST"])
def signupAuth():
	data = dict(request.form)
	print(data)
	usersData = mongo.db.usersData
	result = usersData.find_one({"email": data["email"]})
	print(result)
	if (result):
		return redirect("/signup")
	bcrypt_password = bcrypt.hashpw(str(data["password"]).encode("utf-8"), bcrypt.gensalt(12))
	data["password"] = bcrypt_password
	usersData.insert_one(data)
	return redirect("/login")

# -------------------------------------------------------------------------------------------------------------#

@app.route("/login")
def login():
	return render_template("login.html")

# -------------------------------------------------------------------------------------------------------------#

@app.route('/loginAuth', methods=["POST"])
def loginAuth():
    data = dict(request.form)
    usersData = mongo.db.usersData
    findEmail = usersData.find_one({"email": data['email']})
    if(findEmail):
        checkPassword = bcrypt.checkpw(str(data['password']).encode('utf8'), findEmail['password'])
        if(checkPassword):                             #.encode('utf8')
            return redirect('/home')
        return redirect('/login')
    return redirect('/login')

# -------------------------------------------------------------------------------------------------------------#

# LOGIN AND SIGNUP AUTH -- PYMONGO(DATABASE)

@app.route("/auth", methods=["POST"])  # adding method in app.route so, you should write (methods=["POST"]) in python
def auth():                            # and write (method=["POST"]) in HTML.
	print("===========")
	print(request.form)
	print("===========")
	data = request.form
	
	for i, v in enumerate(users):
		if (data["Email"] == v["Email"] and data["password"] == v["password"]):
			return redirect("/home")
	else:
		return redirect("/login")


if __name__ == '__main__':
	app.run(debug=True)
