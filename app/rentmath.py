from decimal import Decimal



def float_to_percent(num):
    d = Decimal(num*100).quantize(Decimal('.01'))
    return d


def float_to_currency(num):
    '''

    :param num: float
    :return: currency formatted string
    '''
    # truncate float to 2 decimal places
    d = Decimal(num).quantize(Decimal('.01'))
    # add comma for thousands separator
    d = "{:,.2f}".format(d)
    return d

def integer_to_currency(num):
    d = "{:,d}".format(num)
    return d


def do_rental_math(data):
    project_cost = data['purchase_price'] + data['closing_cost'] + data['repair_cost']
    down_payment_amount = data['purchase_price'] * (data['down_payment_percent']/100.0)
    loan_amount = data['purchase_price'] - down_payment_amount

    # Loan monthly payment formula
    # Taken from https://en.wikipedia.org/wiki/Mortgage_calculator#Monthly_payment_formula
    # r = the monthly interest rate, expressed as a decimal, not a percentage
    r = (data['loan_interest_rate_percent'] / 12.0) / 100.0
    # N = the number of monthly payments, the loan period in months
    N = data['loan_period_years'] * 12
    # P = the amount borrowed, known as the loan's principal
    P = loan_amount
    loan_payment = (r*P * pow(1+r, N)) / (pow(1+r, N) - 1)

    cash_needed = down_payment_amount + data['closing_cost'] + data['repair_cost']
    misc_income = data['misc_income_monthly']
    income = data['rental_income_monthly'] + misc_income


    # Expenses other than loan
    property_tax = data['property_tax_annual'] / 12.0
    hazard_insurance = data['hazard_insurance_annual'] / 12.0
    flood_insurance = data['flood_insurance_annual'] / 12.0
    utilities = income * (data['utilities_monthly_percent'] / 100.0)
    vacancy = income * (data['vacancy_monthly_percent'] / 100.0)
    repairs = income * (data['repairs_monthly_percent'] / 100.0)
    capex = income * (data['capex_monthly_percent'] / 100.0)
    management = income * (data['manager_monthly_percent'] / 100.0)
    hoa = data['hoa_monthly']
    misc_expense = data['misc_expense_monthly']

    expenses_total = loan_payment + property_tax + hazard_insurance + flood_insurance +\
        utilities + vacancy + repairs + capex + management + hoa + misc_expense
    expenses_no_mortgage = property_tax + hazard_insurance + flood_insurance +\
        utilities + vacancy + repairs + capex + management + hoa + misc_expense

    # Cash Flow Monthly
    cash_flow = income - expenses_total
    cash_flow_per_unit = cash_flow / data['units_in_property']
    # Net Operating Income Monthly
    net_operating_income = (income - expenses_no_mortgage)
    # Cap Rate - purchase price + closing cost + repairs
    cap_rate = (net_operating_income * 12) / project_cost
    cash_on_cash_return = (cash_flow * 12) / cash_needed

    result = {
        'property_name': data['property_name'],
        'purchase_price': data['purchase_price'],
        'closing_cost': data['closing_cost'],
        'repair_cost': data['repair_cost'],
        'project_cost': project_cost,
        'down_payment_percent': data['down_payment_percent'],
        'down_payment_amount': down_payment_amount,
        'loan_amount': loan_amount,
        'loan_interest_rate_percent': data['loan_interest_rate_percent'],
        'loan_period_years': data['loan_period_years'],
        'cash_needed': cash_needed,
        'rental_income': data['rental_income_monthly'],
        'misc_income': misc_income,
        'total_income': income,
        'loan_payment': loan_payment,
        'property_tax': property_tax,
        'hazard_insurance': hazard_insurance,
        'flood_insurance': flood_insurance,
        'utilities': utilities,
        'utilities_percent': data['utilities_monthly_percent'],
        'vacancy': vacancy,
        'vacancy_percent': data['vacancy_monthly_percent'],
        'repairs': repairs,
        'repairs_percent': data['repairs_monthly_percent'],
        'capex': capex,
        'capex_percent': data['capex_monthly_percent'],
        'management': management,
        'management_percent': data['manager_monthly_percent'],
        'hoa': hoa,
        'misc_expense': misc_expense,
        'expenses_total': expenses_total,
        'expenses_no_mortgage': expenses_no_mortgage,
        'cash_flow': cash_flow,
        'cash_flow_per_unit': cash_flow_per_unit,
        'net_operating_income': net_operating_income,
        'cap_rate': cap_rate,
        'cash_on_cash_return': cash_on_cash_return,
    }

    return result


def rental_main(data):
    r = do_rental_math(data)

    # Create dict to float currency format
    currency = {
        'down_payment_amount': r['down_payment_amount'],
        'loan_amount': r['loan_amount'],
        'cash_needed': r['cash_needed'],
        'rental_income': r['rental_income'],
        'misc_income': r['misc_income'],
        'total_income': r['total_income'],
        'loan_payment': r['loan_payment'],
        'property_tax': r['property_tax'],
        'hazard_insurance': r['hazard_insurance'],
        'flood_insurance': r['flood_insurance'],
        'utilities': r['utilities'],
        'vacancy': r['vacancy'],
        'repairs': r['repairs'],
        'capex': r['capex'],
        'management': r['management'],
        'hoa': r['hoa'],
        'misc_expense': r['misc_expense'],
        'expenses_total': r['expenses_total'],
        'cash_flow': r['cash_flow'],
        'cash_flow_per_unit': r['cash_flow_per_unit'],
        'net_operating_income': r['net_operating_income'],
    }

    for k, v in currency.iteritems():
        r[k] = float_to_currency(v)


    percents = {
        'cap_rate': r['cap_rate'],
        'cash_on_cash_return': r['cash_on_cash_return'],
    }
    for k, v in percents.iteritems():
        r[k] = float_to_percent(v)


    dollars = {
        'purchase_price': r['purchase_price'],
        'closing_cost': r['closing_cost'],
        'repair_cost': r['repair_cost'],
        'project_cost': r['project_cost'],
    }
    for k, v in dollars.iteritems():
        r[k] = integer_to_currency(v)

    # if value is 0, show a dash line '-' instead for readability
    for k, v in currency.iteritems():
        try:
            f = float(v)
            if f == 0.0:
                r[k] = '-'
        except:
            pass




    return r






if __name__ == '__main__':
    data = {
        'property_name': '1 Main St',
        'purchase_price': 200000,
        'closing_cost': 5000,
        'repair_cost': 15000,
        'down_payment_percent': 20,
        'loan_interest_rate_percent': 4.5,
        'loan_period_years': 30,
        'units_in_property': 2,
        'rental_income_monthly': 2000,
        'misc_income_monthly': 0,
        'property_tax_annual': 5000,
        'hazard_insurance_annual': 1200,
        'flood_insurance_annual': 0,
        'utilities_monthly_percent': 0,
        'vacancy_monthly_percent': 8,
        'repairs_monthly_percent': 8,
        'capex_monthly_percent': 8,
        'manager_monthly_percent': 8,
        'hoa_monthly': 0,
        'misc_expense_monthly': 0,
    }
    rental_main(data)







