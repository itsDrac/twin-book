from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, PasswordField, SubmitField
from wtforms.validators import DataRequired, length, Email, NumberRange

class RegisterForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    number = IntegerField('Number', validators=[DataRequired()])
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    password = PasswordField('password', validators=[DataRequired()]) 
    submit = SubmitField('Register')

class LoginForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])
    submit = SubmitField('Login')
