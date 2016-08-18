from system.core.controller import *

class Messages(Controller):
	def __init__(self, action):
		super(Messages, self).__init__(action)
		self.load_model('WelcomeModel')
		self.db = self._app.db

	def create(self, id):
		route = '/users/show/' + id
		return redirect(route)

	def comment(self, id):
		route = '/users/show/' + id
		return redirect(route)