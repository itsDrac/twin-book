from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, PasswordField, SubmitField
from wtforms.validators import DataRequired, length, Email, NumberRange, ValidationError
from app.models import Company

class RegisterForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    number = IntegerField('Number', validators=[DataRequired()])
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    password = PasswordField('password', validators=[DataRequired()]) 
    submit = SubmitField('Register')

    def validate_name(self, name):
        company = Company.query.filter_by(name=name.data).first()
        if company:
            raise ValidationError('Company with this name already exist')

def password_check(form, field):
    company = Company.query.filter_by(name=form.name.data).first()
    if company and company.password != field.data :
        raise ValidationError('Incorrect password')
    elif not company:
        raise ValidationError('Company does not exist')

class LoginForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired(), password_check])
    submit = SubmitField('Login')

