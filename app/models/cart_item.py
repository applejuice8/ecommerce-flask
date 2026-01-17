from app.extensions import db

class CartItem(db.Model):
    __tablename__ = 'cart_item'

    id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True
    )
    cart_id = db.Column(
        db.Integer,
        db.ForeignKey('cart.id'),
        nullable=False
    )
    product_id = db.Column(
        db.Integer,
        db.ForeignKey('product.id'),
        nullable=False
    )
    quantity = db.Column(
        db.Integer,
        nullable=False,
        default=1
    )

    __table_args__ = (
        db.UniqueConstraint('cart_id', 'product_id', name='uq_cart_product'),
    )

    def __repr__(self):
        return f'<CartItem id={self.id}, cart_id={self.cart_id}, product_id={self.product_id}, quantity={self.quantity}>'
