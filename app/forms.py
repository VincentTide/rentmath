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
    property_units = IntegerField()  # default 1 for single family house
    rental_income_monthly = FloatField()  # total rental income
    misc_income_monthly = FloatField()
    property_tax_annual = FloatField()
    hazard_insurance_annual = FloatField()
    flood_insurance_annual = FloatField()
    utilities_monthly_percent = FloatField()
    vacancy_monthly_percent = FloatField()
    repairs_monthly_percent = FloatField()
    capex_monthly_percent = FloatField()
    manager_monthly_percent = FloatField()
    hoa_monthly = FloatField()
    misc_expense_monthly = FloatField()
    submit = SubmitField('Submit')
