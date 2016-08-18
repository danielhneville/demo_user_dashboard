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

	def login(self):
		#if user is admin, return them to the admin dashboard instead.
		return redirect('/dashboard')

	def create(self):
		#if user is normal user who just registered, return them to the dashboard instead.
		return redirect('/dashboard/admin')

	def update(self):
		#grab session data and data from one of the three different forms (based on which was submitted - info, password, description) to update user information through the user model.
		return redirect('/users/edit')