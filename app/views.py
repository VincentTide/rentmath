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

        closing_cost = form.closing_cost.data
        if closing_cost == None:
            closing_cost = 0
        repair_cost = form.repair_cost.data
        if repair_cost == None:
            repair_cost = 0
        property_units = form.property_units.data
        if property_units == None:
            property_units = 1
        misc_income = form.misc_income.data
        if misc_income == None:
            misc_income = 0
        property_tax_annual = form.property_tax_annual.data
        if property_tax_annual == None:
            property_tax_annual = 0
        hazard_insurance_annual = form.hazard_insurance_annual.data
        if hazard_insurance_annual == None:
            hazard_insurance_annual = 0
        flood_insurance_annual = form.flood_insurance_annual.data
        if flood_insurance_annual == None:
            flood_insurance_annual = 0
        utilities_percent = form.utilities_percent.data
        if utilities_percent == None:
            utilities_percent = 0
        vacancy_percent = form.vacancy_percent.data
        if vacancy_percent == None:
            vacancy_percent = 0
        repairs_percent = form.repairs_percent.data
        if repairs_percent == None:
            repairs_percent = 0
        capex_percent = form.capex_percent.data
        if capex_percent == None:
            capex_percent = 0
        management_percent = form.manager_percent.data
        if management_percent == None:
            management_percent = 0
        hoa = form.hoa_monthly.data
        if hoa == None:
            hoa = 0
        misc_expense = form.misc_expense_monthly.data
        if misc_expense == None:
            misc_expense = 0



        data = {
            'property_name': form.property_name.data,
            'purchase_price': form.purchase_price.data,
            'closing_cost': closing_cost,
            'repair_cost': repair_cost,
            'down_payment': form.down_payment_percent.data,
            'interest_rate': form.interest_rate.data,
            'loan_years': form.loan_years.data,
            'property_units': property_units,
            'rental_income': form.rental_income.data,
            'misc_income': misc_income,
            'property_tax_annual': property_tax_annual,
            'hazard_insurance_annual': hazard_insurance_annual,
            'flood_insurance_annual': flood_insurance_annual,
            'utilities_percent': utilities_percent,
            'vacancy_percent': vacancy_percent,
            'repairs_percent': repairs_percent,
            'capex_percent': capex_percent,
            'management_percent': management_percent,
            'hoa': hoa,
            'misc_expense': misc_expense,
        }
        result = rental_main(data)

        return render_template('rental-calculator.html', result=result)
    return redirect(url_for('index', form=form))



