

class UserService(object):

	def __init__(self,users):
		self.users = users

	def userProgramatic(self,name):
		userList = []
		for user in self.users.find():
			if user["name"]==name :
				userList.append(user)
		return userList

	def userQuery(self,name):
		userList = []
		for user in self.users.find({"name": name}):
			userList.append(user)
		return userList