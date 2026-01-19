from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email

class AuthForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])

class LoginForm(AuthForm):
    submit = SubmitField('Log In')

class SignupForm(AuthForm):
    username = StringField('Username', validators=[DataRequired()])
    submit = SubmitField('Sign Up')
