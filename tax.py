import math

tax_brackets = {
    0: 0,
    1: 18200,
    2: 45000,
    3: 120000,
    4: 180000,
    5: math.inf
}

tax_rates = {
    1: 0,
    2: 0.19,
    3: 0.325,
    4: 0.37,
    5: 0.45
}

def netIncome(income):
    if income < tax_brackets[0]:
        return "You're in debt!"
    if income <= tax_brackets[1]:
        return income
    for i in tax_brackets:
        if income <= tax_brackets[i]:            
            nat_accum = [(1- tax_rates[j])*(tax_brackets[j] - tax_brackets[j-1]) for j in range(1, i)]
            net = sum(nat_accum) + (income - tax_brackets[i-1])*(1-tax_rates[i])
            return round(net, 2)

def netIncomeInverse(net_income):
    if net_income  <= 0:
        return "Get outta here!"
    
    bracket = 0
    for i in tax_brackets:
        if net_income <= tax_brackets[i]:
            bracket = i
            break
    
    def solver(index):
        if index == 1:
            return net_income
        
        threshhold = tax_brackets[index-1]
        rate = 1-tax_rates[index]
        
        tot_income = (net_income - netIncome(threshhold) + rate*(threshhold))/rate
        if tot_income <= tax_brackets[index]:
            return tot_income
        else:
            return solver(index + 1)
        
    return solver(bracket)
    
def taxPaid(income):
    print("Is this (1) net income or (2) gross income? \nPlease enter 1 or 2 accordingly.")
    ans = int(input().strip())
    if ans == 1:
        gross = netIncomeInverse(income)
        return round(gross - income, 2)
    if ans == 2:
        net_income = netIncome(income)
        return round(income - net_income, 2)

def taxPaidNet(income):
    gross = netIncomeInverse(income)
    return round(gross - income, 2)

def taxPaidGross(income):
    net_income = netIncome(income)
    return round(income - net_income, 2)
    