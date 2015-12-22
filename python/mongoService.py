from pymongo import MongoClient
from userService import UserService

class MongoService(object):

	def __init__(self):
		self.client = MongoClient()
		self.db = self.client.web
		self.users = self.db.users

		#init services
		self.userService = UserService(self.users)