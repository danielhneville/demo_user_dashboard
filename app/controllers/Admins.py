from system.core.controller import *

class Admins(Controller):
	def __init__(self, action):
		super(Admins, self).__init__(action)
		self.load_model('WelcomeModel')
		self.db = self._app.db

	def admin(self):
		if 'user' not in session:
			return redirect('/')
		return self.load_view('/admin/admin.html')

	def new(self):
		if 'user' not in session:
			return redirect('/')
		return self.load_view('/admin/new.html')

	def edit(self, id):
		if 'user' not in session:
			return redirect('/')
		return self.load_view('/admin/edit.html')

	def destroy(self, id):
		return redirect('dashboard/admin')

	def update(self, id):
		route = 'users/edit/' + str(id)
		return redirect(route)