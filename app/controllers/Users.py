from system.core.controller import *
import datetime

class Users(Controller):
	def __init__(self, action):
		super(Users, self).__init__(action)
		self.load_model('Message')
		self.load_model('User')

	def signin(self):
		return self.load_view('/users/signin.html')

	def register(self):
		return self.load_view('/users/register.html')

	def dashboard(self):
		if 'user' not in session:
			return redirect('/')
		users = self.models['User'].all_users()
		return self.load_view('/users/dashboard.html', users=users)

	def edit(self):
		if 'user' not in session:
			return redirect('/')
		return self.load_view('/users/edit.html')

	def show(self, id):
		if 'user' not in session:
			return redirect('/')
		user = self.models['User'].one_user(id)
		content = self.models['Message'].get_content_by_user_id(id)
		return self.load_view('/users/show.html', user=user, content=content)

	def logoff(self):
		if 'user' in session:
			session.pop('user', None)
		return redirect('/')

	def login(self):
		#if user is admin, return them to the admin dashboard instead.
		return redirect('/dashboard')

	def create(self):
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