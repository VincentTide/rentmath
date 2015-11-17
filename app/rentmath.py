


def calc_rental(data):
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
    rent = data['rental_income_monthly']

    # Expenses other than loan
    property_tax = data['property_tax_annual'] / 12.0
    hazard_insurance = data['hazard_insurance_annual'] / 12.0
    flood_insurance = data['flood_insurance_annual'] / 12.0
    utilities = rent * (data['utilities_monthly_percent'] / 100.0)
    vacancy = rent * (data['vacancy_monthly_percent'] / 100.0)
    repairs = rent * (data['repairs_monthly_percent'] / 100.0)
    capex = rent * (data['capex_monthly_percent'] / 100.0)
    management = rent * (data['manager_monthly_percent'] / 100.0)

    expenses_total = loan_payment + property_tax + hazard_insurance + flood_insurance +\
        utilities + vacancy + repairs + capex + management
    expenses_no_mortgage = property_tax + hazard_insurance + flood_insurance +\
        utilities + vacancy + repairs + capex + management

    # Cash Flow Monthly
    cash_flow = rent - expenses_total
    cash_flow_per_unit = cash_flow / data['units_in_property']
    # Net Operating Income Yearly
    net_operating_income = (rent - expenses_no_mortgage) * 12
    # Cap Rate - purchase price + closing cost + repairs
    cap_rate = net_operating_income / project_cost
    cash_on_cash_return = (cash_flow * 12) / cash_needed

    result = {
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
        'rent': rent,
        'loan_payment': loan_payment,
        'property_tax': property_tax,
        'hazard_insurance': hazard_insurance,
        'flood_insurance': flood_insurance,
        'utilities': utilities,
        'vacancy': vacancy,
        'repairs': repairs,
        'capex': capex,
        'management': management,
        'expenses_total': expenses_total,
        'expenses_no_mortgage': expenses_no_mortgage,
        'cash_flow': cash_flow,
        'cash_flow_per_unit': cash_flow_per_unit,
        'net_operating_income': net_operating_income,
        'cap_rate': cap_rate,
        'cash_on_cash_return': cash_on_cash_return,
    }

    return result



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
        'property_tax_annual': 5000,
        'hazard_insurance_annual': 1200,
        'flood_insurance_annual': 0,
        'utilities_monthly_percent': 0,
        'vacancy_monthly_percent': 8,
        'repairs_monthly_percent': 8,
        'capex_monthly_percent': 8,
        'manager_monthly_percent': 8,
        'hoa_monthly': 0,
        'misc_monthly': 0,
    }
    calc_rental(data)







