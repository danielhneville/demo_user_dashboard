from system.core.controller import *

class Users(Controller):
	def __init__(self, action):
		super(Users, self).__init__(action)

		self.load_model('WelcomeModel')
		self.db = self._app.db

	def signin(self):
		return self.load_view('/users/signin.html')

	def register(self):
		return self.load_view('/users/register.html')

	def dashboard(self):
		return self.load_view('/users/dashboard.html')

	def edit(self):
		return self.load_view('/users/edit.html')

	def show(self, id):
		return self.load_view('/users/show.html')

	def logoff(self):
		return redirect('/')