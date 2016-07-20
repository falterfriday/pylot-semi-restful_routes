""" 
MODEL
"""
from system.core.model import Model

class Product(Model):
    def __init__(self):
        super(Product, self).__init__()

    def get_all_products(self):
        return self.db.query_db("SELECT * FROM products ORDER BY created_at DESC")

    def add_product(self, product):
        query = "INSERT INTO products (name, description, price, created_at, updated_at) VALUES (:name, :description, :price, NOW(), NOW() )"
        data = { 'name': product['name'], 'description': product['description'], 'price': product['price'] }
        return self.db.query_db(query, data)

    def show_product_by_id(self, product_id):
        query = "SELECT * FROM products WHERE id = :product_id"
        data = { 'product_id': product_id }
        return self.db.query_db(query, data)

    def update_product_by_id(self, product):
        query = "UPDATE products SET name=:name, description=:description, price=:price, updated_at=NOW() WHERE id = :id"
        data = { 'name': product['name'], 'description': product['description'], 'price': product['price'], 'id': product['id'] }
        return self.db.query_db(query, data)


    def delete_product_by_id(self, product):
        print product
        query = "DELETE FROM products WHERE id = :product_id"
        data = { "product_id": product['id'] }
        return self.db.query_db(query, data)