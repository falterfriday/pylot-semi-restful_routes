"""
CONTROLLER
"""
from system.core.controller import *

class Products(Controller):
    def __init__(self, action):
        super(Products, self).__init__(action)

        self.load_model('Product')
        self.db = self._app.db


    def index(self):
        products = self.models['Product'].get_all_products()
        return self.load_view('index.html', products=products)
    

    def new(self):
        return self.load_view('new.html')

   
    def create(self):
        if len(request.form['name']) > 0:
            product_details = {
                'name': request.form['name'],
                'description': request.form['description'],
                'price': request.form['price']
            }
            self.models['Product'].add_product(product_details)
            return redirect('/products')
        else:
            flash('name required')
            return redirect('/products/new')
        return redirect('/')


    def show(self, product_id):
        product = self.models['Product'].show_product_by_id(product_id)
        return self.load_view('show.html', product=product)    


    def edit(self, product_id):
        product = self.models['Product'].show_product_by_id(product_id)
        return self.load_view('edit.html', product=product)

    
    def update(self, product_id):
        product = {
        'id': product_id,
        'name': request.form['name'],
        'description': request.form['description'],
        'price': request.form['price']
        }
        self.models['Product'].update_product_by_id(product)
        return redirect('/products')

    def destroy(self, product_id):
        product = {
        'id': product_id
        }
        self.models['Product'].delete_product_by_id(product)
        return redirect('/products')




