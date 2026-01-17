from app.extensions import db

class Product(db.Model):
    __tablename__ = 'product'

    id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True
    )
    name = db.Column(
        db.String(100),
        nullable=False,
    )
    description = db.Column(
        db.String(100),
        nullable=False,
    )
    image = db.Column(
        db.String(500),
        default='static/images/no-image.png'
    )
    cart_items = db.relationship(
        'CartItem',
        backref='product',
        lazy=True
    )

    def __repr__(self):
        return f'<Product id={self.id}, name={self.name}, description={self.description}, image={self.image}>'
