from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, IntegerField, Form, FieldList, FormField, SubmitField, DateField
from wtforms.validators import DataRequired

class VendorProductForm(Form):
    product_id = SelectField('Product' ,coerce=int, validators=[DataRequired()])
    quantity = IntegerField('Quantity', validators=[DataRequired()])

class VendorForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    date = DateField('Current Date', validators=[DataRequired()], format='%d/%m/%y')
    products = FieldList(FormField(VendorProductForm), min_entries=1)

