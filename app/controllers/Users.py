from system.core.controller import *

class Users(Controller):
	def __init__(self, action):
		super(Users, self).__init__(action)

		self.load_model('User')

	def signin(self):
		return self.load_view('/users/signin.html')

	def register(self):
		return self.load_view('/users/register.html')

	def dashboard(self):
		users = self.models['User'].all_users()
		for user in users:
			if user['user_level'] == 9:
				user['user_level'] = 'admin'
			else:
				user['user_level'] = 'normal'
			user['created_at'] = user['created_at'].strftime('%b %d, %Y')
		return self.load_view('/users/dashboard.html', users=users)

	def edit(self):
		return self.load_view('/users/edit.html')

	def show(self, id):
		return self.load_view('/users/show.html')

	def logoff(self):
		if 'user' in session:
			session.pop('user', None)
		return redirect('/')

	def login(self):
		#if user is admin, return them to the admin dashboard instead.
		return redirect('/dashboard')

	def create(self):
		#if user is normal user who just registered, return them to the dashboard instead.
		user = self.models['User'].insert_user(request.form)
		if not user:
			return redirect('/')
		else:
			session['user'] = user
			if user['user_level'] == 9:
				return redirect('/dashboard/admin')
			else:
				return redirect('/dashboard')

	def update(self):
		#grab session data and data from one of the three different forms (based on which was submitted - info, password, description) to update user information through the user model.
		return redirect('/users/edit')