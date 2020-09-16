from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, IntegerField, Form, FieldList, FormField, SubmitField
from wtforms.validators import DataRequired

class ItemQuantityForm(Form):
    item_id = SelectField('Item', coerce=int,  validators=[DataRequired()])
    quantity = IntegerField('Quantity', validators=[DataRequired()])

class ProductForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    item_quantity = FieldList(FormField(ItemQuantityForm), min_entries=1)
    stock = IntegerField('Stock', validators=[DataRequired()])
    submit = SubmitField('Save')
