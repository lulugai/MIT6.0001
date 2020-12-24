annual_salary = float(input('Enter your  starting annual salary:'))
total_cost = 1000000
semi_annual_raise = 0.07

portion_down_payment = 0.25
current_savings = 0
r = 0.04
monthly_salary = annual_salary/12
num_months = 0
low = 0
high = 1
portion_saved = (high + low)/2.0
step = 0

while abs(current_savings - total_cost*portion_down_payment) >=100:
    while  num_months < 36:
        current_savings += current_savings*r/12
        current_savings += monthly_salary*portion_saved
        if (num_months/6) >= 1 and num_months%6 ==0:
            monthly_salary += monthly_salary*semi_annual_raise
        num_months +=1

    if current_savings <= total_cost*portion_down_payment:
        low = portion_saved
    else:
        high = portion_saved
    portion_saved = (high + low)/2.0
    step +=1
    num_months = 0

print('Best saving rate: %.4f',portion_saved)
print('Steps in bisection search:',step)

