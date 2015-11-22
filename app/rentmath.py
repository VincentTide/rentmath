from decimal import Decimal


def round_float_2(num):
    d = Decimal(num).quantize(Decimal('.01'))
    return d


def rental_main(data):
    # the dicts to hold our values in
    decs = {}
    dollars = {}
    percents = {}
    result = {}


    dollars['purchase_price'] = data['purchase_price']
    dollars['closing_cost'] = data['closing_cost']
    dollars['repair_cost'] = data['repair_cost']
    dollars['project_cost'] = dollars['purchase_price'] + dollars['closing_cost'] + dollars['repair_cost']

    decs['down_payment'] = data['down_payment']
    decs['down_payment_amount'] = dollars['purchase_price'] * (decs['down_payment'] / 100.0)
    decs['loan_amount'] = dollars['purchase_price'] - decs['down_payment_amount']

    # Loan monthly payment formula
    # Taken from https://en.wikipedia.org/wiki/Mortgage_calculator#Monthly_payment_formula
    # r = the monthly interest rate, expressed as a decimal, not a percentage
    r = (data['interest_rate'] / 12.0) / 100.0
    # N = the number of monthly payments, the loan period in months
    N = data['loan_years'] * 12
    # P = the amount borrowed, known as the loan's principal
    P = decs['loan_amount']
    decs['loan_payment'] = (r*P * pow(1+r, N)) / (pow(1+r, N) - 1)

    decs['cash_needed'] = decs['down_payment_amount'] + dollars['closing_cost'] + dollars['repair_cost']

    # We need to truncate to 2 precision
    decs['rental_income'] = round_float_2(data['rental_income'])
    decs['misc_income'] = round_float_2(data['misc_income'])
    decs['total_income'] = decs['rental_income'] + decs['misc_income']
    decs['total_income'] = float(decs['total_income'])

    # Expenses other than loan
    decs['property_tax'] = data['property_tax_annual'] / 12.0
    decs['insurance'] = data['insurance_annual'] / 12.0
    decs['utilities'] = decs['total_income'] * (data['utilities_percent'] / 100.0)
    decs['vacancy'] = decs['total_income'] * (data['vacancy_percent'] / 100.0)
    decs['repairs'] = decs['total_income'] * (data['repairs_percent'] / 100.0)
    decs['capex'] = decs['total_income'] * (data['capex_percent'] / 100.0)
    decs['management'] = decs['total_income'] * (data['management_percent'] / 100.0)
    decs['hoa'] = data['hoa']
    decs['misc_expense'] = data['misc_expense']

    # Round to 2 precision
    for key, value in decs.iteritems():
        decs[key] = round_float_2(value)

    decs['expenses_total'] = decs['loan_payment'] + \
                             decs['property_tax'] + \
                             decs['insurance'] +\
                             decs['utilities'] +\
                             decs['vacancy'] +\
                             decs['repairs'] +\
                             decs['capex'] +\
                             decs['management'] +\
                             decs['hoa'] +\
                             decs['misc_expense']
    decs['expenses_no_mortgage'] = decs['property_tax'] + \
                                   decs['insurance'] +\
                                   decs['utilities'] +\
                                   decs['vacancy'] +\
                                   decs['repairs'] +\
                                   decs['capex'] +\
                                   decs['management'] +\
                                   decs['hoa'] +\
                                   decs['misc_expense']

    # cash flow monthly
    decs['cash_flow'] = decs['total_income'] - decs['expenses_total']
    decs['cash_flow_per_unit'] = decs['cash_flow'] / data['property_units']
    # net operating income monthly
    decs['net_operating_income'] = decs['total_income'] - decs['expenses_no_mortgage']
    # cap rate - purchase price + closing cost + repairs
    percents['cap_rate'] = (decs['net_operating_income'] * 12) / dollars['project_cost']
    percents['cash_on_cash_return'] = (decs['cash_flow'] * 12) / decs['cash_needed']

    # Round to 2 precision and add comma to thousand separate
    for key, value in decs.iteritems():
        if value == 0.0:
            decs[key] = '-'
        else:
            decs[key] = "{:,.2f}".format(round_float_2(value))

    # Round percents to 2 precision
    for key, value in percents.iteritems():
        percents[key] = Decimal(value*100).quantize(Decimal('.01'))

    # add thousand separator
    for key, value in dollars.iteritems():
        if value == 0:
            dollars[key] = '-'
        else:
            dollars[key] = "{:,d}".format(value)

    # add any other vars we want to return
    result = {
        'property_name' : data['property_name'],
        'interest_rate': data['interest_rate'],
        'loan_years': data['loan_years'],
        'utilities_percent': data['utilities_percent'],
        'vacancy_percent': data['vacancy_percent'],
        'repairs_percent': data['repairs_percent'],
        'capex_percent': data['capex_percent'],
        'management_percent': data['management_percent'],
        'property_units': data['property_units'],
    }
    result.update(percents)
    result.update(dollars)
    result.update(decs)
    return result


if __name__ == '__main__':
    data = {
        'property_name': '1 Main St',
        'purchase_price': 200000,
        'closing_cost': 5000,
        'repair_cost': 15000,
        'down_payment': 20,
        'interest_rate': 4.5,
        'loan_years': 30,
        'property_units': 2,
        'rental_income': 2000,
        'misc_income': 0,
        'property_tax_annual': 5000,
        'insurance_annual': 1200,
        'utilities_percent': 0,
        'vacancy_percent': 8,
        'repairs_percent': 8,
        'capex_percent': 8,
        'management_percent': 8,
        'hoa': 0,
        'misc_expense': 0,
    }
    rental_main(data)







