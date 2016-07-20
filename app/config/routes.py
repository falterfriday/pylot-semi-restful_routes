
from system.core.router import routes

routes['default_controller'] = 'Products'
routes['/products'] = 'Products#index'
routes['/products/new'] = 'Products#new'
routes['POST']['/products/new/create'] = 'Products#create'
routes['/products/show/<product_id>'] = 'Products#show'
routes['/products/edit/<product_id>'] = 'Products#edit'
routes['POST']['/products/update/<product_id>'] = 'Products#update'
routes['POST']['/products/delete/<product_id>'] = 'Products#destroy'
