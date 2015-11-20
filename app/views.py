from app import app
from flask import request, render_template, redirect, url_for, flash, abort, make_response, session, send_from_directory
from forms import RentalIncomeCalculatorForm
from rentmath import *
import json
import base64


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.route('/', methods=['GET'])
def index():
    form = RentalIncomeCalculatorForm()
    return render_template('index.html', form=form)


@app.route('/rental', methods=['GET'])
def rental():
    form = RentalIncomeCalculatorForm()
    pass


# @app.route('/rental/<string:token>', methods=['GET'])
# def rental_token(token):
#     form = RentalIncomeCalculatorForm()
#     print token
#     decoded = base64.urlsafe_b64decode(str(token))
#     data = json.loads(decoded)
#     result = rental_main(data)
#     return render_template('rental-calculator.html', result=result)



@app.route('/rental', methods=['POST'])
def rental_post():
    form = RentalIncomeCalculatorForm()
    if form.validate_on_submit():
        data = {
            'property_name': form.property_name.data,
            'purchase_price': form.purchase_price.data,
            'closing_cost': form.closing_cost.data,
            'repair_cost': form.repair_cost.data,
            'down_payment_percent': form.down_payment_percent.data,
            'loan_interest_rate_percent': form.loan_interest_rate_percent.data,
            'loan_period_years': form.loan_period_years.data,
            'property_units': form.property_units.data,
            'rental_income_monthly': form.rental_income_monthly.data,
            'misc_income_monthly': form.misc_income_monthly.data,
            'property_tax_annual': form.property_tax_annual.data,
            'hazard_insurance_annual': form.hazard_insurance_annual.data,
            'flood_insurance_annual': form.flood_insurance_annual.data,
            'utilities_monthly_percent': form.utilities_monthly_percent.data,
            'vacancy_monthly_percent': form.vacancy_monthly_percent.data,
            'repairs_monthly_percent': form.repairs_monthly_percent.data,
            'capex_monthly_percent': form.capex_monthly_percent.data,
            'management_monthly_percent': form.manager_monthly_percent.data,
            'hoa': form.hoa_monthly.data,
            'misc_expense': form.misc_expense_monthly.data,
        }
        result = rental_main(data)

        # Create a base64 encoded string of the data
        # dump = json.dumps(data)
        # encoded = base64.urlsafe_b64encode(dump)
        # return redirect(url_for('rental_token', token=encoded))


        # Create query string
        # qs = '/rental?'
        # for key, value in data.iteritems():
        #     qs += "{0}={1}&".format(key, value)
        # qs = qs[:-1]



        return render_template('rental-calculator.html', result=result)
    return redirect(url_for('index', form=form))



