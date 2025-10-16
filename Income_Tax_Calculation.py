def income_tax_single(income, round_income = True):
    
    if round_income == True:
        income = round(income) # round to nearest integer
    else:
        income = income # do not round it
    
    if income <= 9875:
        tax_bracket = 0.10
        income_tax = 0.10 * income
    elif income <= 40125:
        tax_bracket = 0.12
        income_tax = 987.50 + 0.12 * (income - 9875)
    elif income <= 85525:
        tax_bracket = 0.22
        income_tax = 4617.50 + 0.22 * (income - 40125)
    elif income <= 163300:
        tax_bracket = 0.24
        income_tax = 14605.50 + 0.24 * (income - 85525)
    elif income <= 207350:
        tax_bracket = 0.32
        income_tax = 33271.50 + 0.32 * (income - 163300)
    elif income <= 518400:
        tax_bracket = 0.35
        income_tax = 47367.50 + 0.35 * (income - 207350)
    else:  # income > 518400
        tax_bracket = 0.37
        income_tax = 156235 + 0.37 * (income - 518400)
    
    return income_tax, tax_bracket

import numpy as np
import matplotlib.pyplot as plt
income_range = range(1,1000000,1000)
tax, tax_bracket = np.vectorize(income_tax_single)(income_range)
plt.plot(income_range,tax)
plt.xlabel('Income (Dollars)')
plt.ylabel('Income Tax Owed (Dollars)')
plt.grid('on')
plt.title("Single payer")

import matplotlib.pyplot as plt
effective_tax_rate = tax/income_range
plt.plot(income_range,effective_tax_rate * 100, label = 'effective rate')
plt.plot(income_range,tax_bracket * 100, label = 'tax bracket')
plt.legend(["effective rate","tax bracket"])
plt.xlabel('Income (Dollars)')
plt.ylabel('Tax Rate Percentage')
plt.title('Single Payer')
plt.grid('on')

def income_tax_married_jointly(income):
    
    income = round(income) ## round the income to nearest integer

    if income <= 19750:
        tax_bracket = 0.10
        income_tax = 0.10 * income
    elif income <= 80250:
        tax_bracket = 0.12
        income_tax = 1975 + 0.12 * (income - 19750)
    elif income <= 171050:
        tax_bracket = 0.22
        income_tax = 9235 + 0.22 * (income - 80250)
    elif income <= 326600:
        tax_bracket = 0.24
        income_tax = 29211 + 0.24 * (income - 171050)
    elif income <= 414700:
        tax_bracket = 0.32
        income_tax = 66543 + 0.32 * (income - 326600)
    elif income <= 622050:
        tax_bracket = 0.35
        income_tax = 94735 + 0.35 * (income - 414700)
    else:  # income >= 622051
        tax_bracket = 0.37
        income_tax = 167307.50 + 0.37 * (income - 622050)

    return income_tax, tax_bracket

import numpy as np
import matplotlib.pyplot as plt
income_range = range(1,1000000,1000)
tax, tax_bracket = np.vectorize(income_tax_married_jointly)(income_range)
plt.plot(income_range,tax)
plt.xlabel('Joint Income (Dollars)')
plt.ylabel('Joint Income Tax Owed (Dollars)')
plt.grid('on')
plt.title("Married payers filing jointly")

import matplotlib.pyplot as plt
effective_tax_rate = tax/income_range
plt.plot(income_range,effective_tax_rate * 100, label = 'effective rate')
plt.plot(income_range,tax_bracket * 100 , label = 'tax bracket')
plt.legend(["effective rate","tax bracket"])
plt.xlabel('Income (Dollars)')
plt.ylabel('Tax Rate Percentage')
plt.grid('on')

def income_tax(income, status = "single"):
    '''
    Returns income tax based on whether the filing status is 'single' or 'married filing jointly'.

    Call signatures::

    income_tax(income, status = 'single') 
    income_tax(income, status = 'married filing jointly')
    income_tax(income) # will assume status = 'single'

    Assumptions:
    income is rounded off to nearest integer.
    '''
    income = round(income)
    
    if status == 'single':
        tax_owed, tax_bracket  = income_tax_single(income)
    elif status == 'married filing jointly':
        tax_owed, tax_bracket = income_tax_married_jointly(income)
    else:
        print("Status must be either 'single' or 'married filing jointly'. You entered status =", status)
        return
    
    return tax_owed

income_tax(10000, 'single')
income_tax(10000,'married filing jointly')

#modular programming
help(income_tax)
