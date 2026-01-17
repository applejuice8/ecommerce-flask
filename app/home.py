from flask import Blueprint, render_template
from flask_login import login_required, current_user
from app.models import Product, Cart
from app.extensions import db

bp = Blueprint('home', __name__)

@bp.route('/')
@login_required
def index():
    # Get all products
    products = Product.query.all()
    
    # Get user's cart
    cart = Cart.query.filter_by(user_id=current_user.id).first()
    if not cart:
        cart = Cart(user_id=current_user.id)
        db.session.add(cart)
        db.session.commit()
    
    return render_template('index.html', products=products, cart=cart)
