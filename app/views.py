from app import app
from flask import request, render_template, redirect, url_for, flash, abort, make_response, session
from forms import RentalIncomeCalculatorForm
from rentmath import *


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.route('/', methods=['GET'])
def index():
    form = RentalIncomeCalculatorForm()
    return render_template('index.html', form=form)


@app.route('/rental', methods=['GET'])
def rental():
    data = {}
    try:
        data['property_name'] = request.args.get('property_name')
        data['purchase_price'] = int(request.args.get('purchase_price'))
        data['closing_cost'] = int(request.args.get('closing_cost'))
        data['repair_cost'] = int(request.args.get('repair_cost'))
        data['down_payment'] = float(request.args.get('down_payment'))
        data['interest_rate'] = float(request.args.get('interest_rate'))
        data['loan_years'] = int(request.args.get('loan_years'))
        data['property_units'] = int(request.args.get('property_units'))
        data['rental_income'] = float(request.args.get('rental_income'))
        data['misc_income'] = float(request.args.get('misc_income'))
        data['property_tax_annual'] = float(request.args.get('property_tax_annual'))
        data['insurance_annual'] = float(request.args.get('insurance_annual'))
        data['utilities_percent'] = float(request.args.get('utilities_percent'))
        data['vacancy_percent'] = float(request.args.get('vacancy_percent'))
        data['repairs_percent'] = float(request.args.get('repairs_percent'))
        data['capex_percent'] = float(request.args.get('capex_percent'))
        data['management_percent'] = float(request.args.get('management_percent'))
        data['hoa'] = float(request.args.get('hoa'))
        data['misc_expense'] = float(request.args.get('misc_expense'))
    except:
        return redirect(url_for('index'))

    result = rental_main(data)

    qs = '/rental?'
    for key, value in data.iteritems():
        qs += "{0}={1}&".format(key, value)
    qs = qs[:-1]

    return render_template('rental-calculator.html', result=result, qs=qs)


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
        insurance_annual = form.insurance_annual.data
        if insurance_annual == None:
            insurance_annual = 0
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
            'insurance_annual': insurance_annual,
            'utilities_percent': utilities_percent,
            'vacancy_percent': vacancy_percent,
            'repairs_percent': repairs_percent,
            'capex_percent': capex_percent,
            'management_percent': management_percent,
            'hoa': hoa,
            'misc_expense': misc_expense,
        }

        # query string generation
        qs = '/rental?'
        for key, value in data.iteritems():
            qs += "{0}={1}&".format(key, value)
        qs = qs[:-1]

        return redirect(qs)
    return redirect(url_for('index', form=form))



