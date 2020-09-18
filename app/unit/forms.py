from app.models import Unit
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, PasswordField, SubmitField
from wtforms.validators import DataRequired, length, Email, NumberRange, ValidationError

class UnitForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    submit = SubmitField('Add')

    def validate_name(self, name):
        unit = Unit.query.filter_by(name=name.data).first()
        if unit :
            raise ValidationError('Unit with this name already exist')


