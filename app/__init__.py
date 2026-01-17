from flask import Flask
from app.extensions import db, login_manager

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    # Initialize plugins
    db.init_app(app)
    login_manager.init_app(app)

    from app.models import User, Product, Cart, CartItem

    with app.app_context():
        # Create db tables
        db.create_all()
        print('created')

        # Register blueprints
        from .home import bp as home_bp
        from .auth import bp as auth_bp
        from .cart import bp as cart_bp
        
        app.register_blueprint(home_bp)
        app.register_blueprint(auth_bp)
        app.register_blueprint(cart_bp)

        return app
