from flask import Blueprint, render_template
from flask_login import login_required, current_user
from app.models import Product, Cart
from app.extensions import redis_client
import json

bp = Blueprint('home', __name__)

@bp.route('/')
@login_required
def index():
    cached = redis_client.get('products:all')
    if cached:
        products = json.loads(cached)
    else:
        products = [p.to_dict() for p in Product.query.all()]
        redis_client.setex('products:all', 60, json.dumps(products))

    cart = Cart.query.filter_by(user_id=current_user.id).first()

    in_cart = {}
    for cart_item in cart.items:
        in_cart[cart_item.product_id] = cart_item.quantity

    return render_template('index.html', products=products, in_cart=in_cart)
