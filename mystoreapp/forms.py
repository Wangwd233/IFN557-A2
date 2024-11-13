from flask_wtf import FlaskForm
from wtforms.fields import SubmitField, StringField
from wtforms.validators import InputRequired, email

#checkout form for basket
class CheckoutForm(FlaskForm):
    firstname = StringField("First name", validators=[InputRequired()])
    lastname = StringField("Last name", validators=[InputRequired()])
    phone = StringField("Phone number", validators=[InputRequired()])
    email = StringField("Email address", validators=[InputRequired(), email()])
    address = StringField("Shipping Address", validators=[InputRequired()])
    submit = SubmitField("Confirm your contact detail")