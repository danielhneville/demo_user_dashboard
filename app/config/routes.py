from system.core.router import routes

routes['default_controller'] = 'Welcome'

routes['GET']['/signin'] = 'Users#signin'
routes['GET']['/register'] = 'Users#register'
routes['GET']['/dashboard'] = 'Users#dashboard'
routes['GET']['/users/edit'] = 'Users#edit'
routes['GET']['/users/show/<id>'] = 'Users#show'

routes['GET']['/dashboard/admin'] = 'Admins#admin'
routes['GET']['/users/new'] = 'Admins#new'
routes['GET']['/users/edit/<id>'] = 'Admins#edit'

routes['GET']['/logoff'] = 'Users#logoff'

routes['GET']['/admin/destroy/<id>'] = 'Admins#destroy'
routes['POST']['/admin/update/<id>'] = 'Admins#update'