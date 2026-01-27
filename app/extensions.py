from flask_sqlalchemy import SQLAlchemy
from flask_redis import FlaskRedis
from flask_login import LoginManager
from flask_wtf import CSRFProtect

db = SQLAlchemy()
redis_client = FlaskRedis()
login_manager = LoginManager()
csrf = CSRFProtect()

login_manager.login_view = 'auth.login'

@login_manager.user_loader
def load_user(user_id):
    from app.models import User
    return User.query.get(int(user_id))
