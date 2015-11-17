from flask.ext.wtf import Form
from wtforms import StringField, PasswordField, BooleanField, SubmitField, FloatField, IntegerField
from wtforms.validators import DataRequired


class RentalIncomeCalculatorForm(Form):
    property_name = StringField()
    purchase_price = IntegerField(validators=[DataRequired()])
    closing_cost = IntegerField()
    repair_cost = IntegerField()
    down_payment_percent = FloatField()
    loan_interest_rate_percent = FloatField()
    loan_period_years = IntegerField()
    units_in_property = IntegerField()  # default 1 for single family house
    rental_income_monthly = IntegerField()  # total rental income
    property_tax_annual = IntegerField()
    hazard_insurance_annual = IntegerField()
    flood_insurance_annual = IntegerField()
    utilities_monthly_percent = FloatField()
    vacancy_monthly_percent = FloatField()
    repairs_monthly_percent = FloatField()
    capex_monthly_percent = FloatField()
    manager_monthly_percent = FloatField()
    hoa_monthly = IntegerField()
    misc_monthly = IntegerField()
    submit = SubmitField('Submit')
