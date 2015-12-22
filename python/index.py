from flask import Flask
from mongoService import MongoService
from userService import UserService

app = Flask(__name__)
mongoService = MongoService()
userService = mongoService.userService

@app.route("/")
def hello():
	return str(userService.userProgramatic("George") + userService.userQuery("Qvor"))

if __name__ == "__main__":
	app.run(host="localhost",port=5003,debug=True)