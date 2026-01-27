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
    price = db.Column(
        db.Float,
        nullable=False
    )
    image = db.Column(
        db.String(500),
        default='no-image.jpg'
    )

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'price': self.price,
            'image': self.image,
        }

    def __repr__(self):
        return f'<Product id={self.id}, name={self.name}, description={self.description}, price={self.price}, image={self.image}>'
