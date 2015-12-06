from flask.ext.wtf import Form
from wtforms import StringField, PasswordField, BooleanField, SubmitField, FloatField, IntegerField
from wtforms.validators import DataRequired, Optional


class RentalIncomeCalculatorForm(Form):
    property_name = StringField(validators=[Optional()])
    purchase_price = IntegerField(validators=[DataRequired()])
    closing_cost = IntegerField(validators=[Optional()])
    repair_cost = IntegerField(validators=[Optional()])
    down_payment_percent = FloatField(validators=[Optional()])
    interest_rate = FloatField()
    loan_years = IntegerField()
    property_units = IntegerField(validators=[Optional()])
    rental_income = FloatField()
    misc_income = FloatField(validators=[Optional()])
    property_tax_annual = FloatField(validators=[Optional()])
    insurance_annual = FloatField(validators=[Optional()])
    utilities_percent = FloatField(validators=[Optional()])
    vacancy_percent = FloatField(validators=[Optional()])
    repairs_percent = FloatField(validators=[Optional()])
    capex_percent = FloatField(validators=[Optional()])
    manager_percent = FloatField(validators=[Optional()])
    hoa_monthly = FloatField(validators=[Optional()])
    misc_expense_monthly = FloatField(validators=[Optional()])
    submit = SubmitField('Submit')
