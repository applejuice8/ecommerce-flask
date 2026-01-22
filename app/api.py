from flask import Blueprint, flash, request, jsonify
from flask_login import login_required, current_user
from app.models import Cart, CartItem, Product
from app.extensions import db

bp = Blueprint('api', __name__)

@bp.route('/cart/add/<int:product_id>', methods=['POST'])
@login_required
def add_to_cart(product_id: int):
    cart = Cart.query.filter_by(user_id=current_user.id).first()
    product = Product.query.get_or_404(product_id)
    
    # Check if item already in cart
    cart_item = CartItem.query.filter_by(
        cart_id=cart.id,
        product_id=product_id
    ).first()
    
    if cart_item:
        cart_item.quantity += 1
    else:
        cart_item = CartItem(
            cart_id=cart.id,
            product_id=product_id,
            quantity=1
        )
        db.session.add(cart_item)
    
    db.session.commit()
    flash(f'{product.name} added to cart!', 'success')
    
    return jsonify({ 'quantity': cart_item.quantity })

@bp.route('/cart/update/<int:product_id>', methods=['POST'])
@login_required
def update_cart(product_id: int):
    cart = Cart.query.filter_by(user_id=current_user.id).first()
    cart_item = CartItem.query.filter_by(
        cart_id=cart.id,
        product_id=product_id
    ).first()

    data = request.get_json()
    action = data.get('action')
    
    match action:
        case 'increase':
            cart_item.quantity += 1
            flash('Cart updated', 'success')

        case 'decrease':
            if cart_item.quantity <= 1:
                db.session.delete(cart_item)
                flash('Item removed from cart', 'success')
            else:
                cart_item.quantity -= 1
                flash('Cart updated', 'success')
    
        case 'add':
            add_to_cart(product_id)

        case _:
            flash('Invalid action', 'error')

    db.session.commit()

    return jsonify({ 'quantity': cart_item.quantity })
