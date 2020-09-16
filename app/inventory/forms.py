from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, PasswordField, SubmitField
from wtforms.validators import DataRequired, length, Email, NumberRange, ValidationError

class InventoryForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    submit = SubmitField('Add')

    def validate_name(self, name):
        item = Inventory.query.first(name=name.data)
        if item :
            raise ValidationError('Item with this name already exist')

