from flask import Flask
from app.extensions import db, redis_client, login_manager, csrf
from app.errors import register_error_handlers

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    # Initialize plugins
    db.init_app(app)
    redis_client.init_app(app)
    login_manager.init_app(app)
    csrf.init_app(app)

    from app.models import User, Product, Cart, CartItem

    with app.app_context():
        # Create db tables
        db.create_all()

        # Register blueprints
        from .home import bp as home_bp
        from .auth import bp as auth_bp
        from .cart import bp as cart_bp
        from .api import bp as api_bp
        
        app.register_blueprint(home_bp)
        app.register_blueprint(auth_bp, url_prefix='/auth')
        app.register_blueprint(cart_bp, url_prefix='/cart')
        app.register_blueprint(api_bp, url_prefix='/api')

        register_error_handlers(app)

        return app
