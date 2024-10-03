from models import db, Category, Product
from app import app
from random import choice as rc

categories_names = ['Electronics', 'Books', 'Clothing', 'Sports', 'Toys']
products_names = [
    'Laptop', 'Smartphone', 'Headphones', 'Novel', 'Biography',
    'T-Shirt', 'Jeans', 'Football', 'Doll', 'Puzzle',
    'Camera', 'Smartwatch', 'Sneakers', 'Backpack', 'Board Game'
]
with app.app_context():
    Category.query.delete()
    Product.query.delete()
    
    categories = []
    for name in categories_names:
        category = Category(name=name)
        categories.append(category)
    db.session.add_all(categories)
    products =[]
    for name in products_names:
        product = Product(name=name, price=round(rc(range(5, 500)), 2), category=rc(categories))
        products.append(product)
    db.session.add_all(products)
    db.session.commit()