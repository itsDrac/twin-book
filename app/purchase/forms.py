from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, IntegerField, Form, FieldList, FormField, SubmitField, DateField, FloatField
from wtforms.validators import DataRequired

class ItemQuantityForm(Form):
    item_id = SelectField('Item', coerce=int,  validators=[DataRequired()])
    unit_id = SelectField('Unit', coerce=int,  validators=[DataRequired()])
    quantity = IntegerField('Quantity', validators=[DataRequired()])
    price = FloatField('Price' ,validators=[DataRequired()])

class PurchaseForm(FlaskForm):
    name = StringField('Party Name', validators=[DataRequired()])
    current_date = DateField('Current Date', validators=[DataRequired()], format='%d/%m/%y')
    suplier_date = DateField('Suplier Date', validators=[DataRequired()], format='%d/%m/%y')
    invoice = StringField('Invoice Number', validators=[DataRequired()])
    item_quantity = FieldList(FormField(ItemQuantityForm), min_entries=1)
    submit = SubmitField('Save')

