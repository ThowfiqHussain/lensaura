from flask import Flask, render_template, jsonify, request
import json
import os

app = Flask(__name__)

# JSON file load pannra function
def load_products():
    with open('products.json', 'r') as f:
        return json.load(f)

# Home page
@app.route('/')
def home():
    return render_template('index.html')

# Category page - mens / womens / kids
@app.route('/category/<category_name>')
def category(category_name):
    products = load_products()
    category_products = products.get(category_name, [])
    return render_template('category.html', 
                         products=category_products, 
                         category=category_name)

# API - All products (JS fetch use pannum)
@app.route('/api/products')
def get_all_products():
    products = load_products()
    return jsonify(products)

# API - Category products
@app.route('/api/products/<category_name>')
def get_category_products(category_name):
    products = load_products()
    category_products = products.get(category_name, [])
    return jsonify(category_products)

# Cart page
@app.route('/cart')
def cart():
    return render_template('cart.html')

if __name__ == '__main__':
    app.run(debug=True)