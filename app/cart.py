from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from app.models import Cart, CartItem, Product
from app.extensions import db

bp = Blueprint('cart', __name__)

@bp.route('/cart')
@login_required
def view_cart():
    cart = Cart.query.filter_by(user_id=current_user.id).first()
    
    return render_template('cart.html', cart=cart)

@bp.route('/cart/add/<int:product_id>', methods=['POST'])
@login_required
def add_to_cart(product_id: int):
    cart = Cart.query.filter_by(user_id=current_user.id).first()
    product = Product.query.get_or_404(product_id)
    
    # Check if item already in cart
    cart_item = CartItem.query.filter_by(cart_id=cart.id, product_id=product_id).first()
    
    if cart_item:
        cart_item.quantity += 1
    else:
        cart_item = CartItem(cart_id=cart.id, product_id=product_id, quantity=1)
        db.session.add(cart_item)
    
    db.session.commit()
    flash(f'{product.name} added to cart!', 'success')
    
    return redirect(url_for('home.index'))

@bp.route('/cart/remove/<int:product_id>', methods=['POST'])
@login_required
def remove_from_cart(product_id: int):
    cart = Cart.query.filter_by(user_id=current_user.id).first()
    cart_item = CartItem.query.get_or_404(cart_id=cart.id, product_id=product_id)
    
    db.session.delete(cart_item)
    db.session.commit()
    
    flash('Item removed from cart', 'success')
    return redirect(url_for('cart.view_cart'))

@bp.route('/cart/update/<int:product_id>', methods=['POST'])
@login_required
def update_cart(product_id: int):
    cart = Cart.query.filter_by(user_id=current_user.id).first()
    cart_item = CartItem.query.get_or_404(cart_id=cart.id, product_id=product_id)

    quantity = request.form.get('quantity', type=int)
    
    if quantity > 0:
        cart_item.quantity = quantity
        db.session.commit()
        flash('Cart updated', 'success')
    else:
        db.session.delete(cart_item)
        db.session.commit()
        flash('Item removed from cart', 'success')
    
    return redirect(url_for('cart.view_cart'))

@bp.route('/cart/clear', methods=['POST'])
@login_required
def clear_cart():
    cart = Cart.query.filter_by(user_id=current_user.id).first()
    
    if cart:
        # Remove all items
        CartItem.query.filter_by(cart_id=cart.id).delete()
        db.session.commit()
        flash('Cart cleared', 'success')
    
    return redirect(url_for('cart.view_cart'))
