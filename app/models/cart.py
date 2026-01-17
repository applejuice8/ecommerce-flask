from app.extensions import db

class Cart(db.Model):
    __tablename__ = 'cart'

    id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True
    )
    user_id = db.Column(
        db.Integer,
        db.ForeignKey('user.id'),
        nullable=False
    )
    items = db.relationship(
        'CartItem',
        backref='cart',
        lazy=True,
        cascade='all, delete-orphan'
    )

    def __repr__(self):
        return f'<Cart id={self.id}, user_id={self.user_id}, items={self.items}>'
