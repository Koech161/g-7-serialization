from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy_serializer import SerializerMixin

convention = {
    "ix" : "ix_%(column_0_label)s",
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}
metadata = MetaData(naming_convention=convention)
db = SQLAlchemy(metadata=metadata)

class Category(db.Model, SerializerMixin):
    __tablename__ = 'categories'
    serialize_rules = ('-products.category',)
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    
    products = db.relationship('Product', back_populates='category')

    def __repr__(self):
        return f'<Category {self.id}, {self.name}>'
class Product(db.Model, SerializerMixin):
    __tablename__ = 'products'
    serialize_rules = ('-category.products',)
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'))

    category = db.relationship('Category', back_populates='products')

    def __repr__(self):
        return f'<Product {self.id}, {self.name}, {self.price}>'