# User Input
annual_salary_str = input("Enter your annual salary: ")
annual_salary = float(annual_salary_str) 

# hardcoded variables
total_cost = 1000000 
semi_annual_raise = 0.07 
current_savings = 0.00
months_required = 36
bisection_count = 0


# derived variables
monthly_salary = annual_salary / 12
portion_downpayment = 0.25 * total_cost                             # 25% downpayment specified in requirements
start_rate = 0
end_rate = 10000


# func calculateSavings
def calculateSavings(rate,semi_annual_raise,monthly_salary):
    """
        Inputs : 
            1. rate                    => int, % rate of instrest.Will be divided by 10000. eg: 4500 which is 4.5%
            2. semi_annual_raise       => float, % raise after 6 months. eg: 0.03
            3. monthly salary          => int, montly salary
        Output :
            float, This function will calculate the savings at the end of 36 months for a given rate of savings, semi-annual raise and salary.

        Caveats:
        range function needs to be from 1 to 37 because raise should be not be applied on 0th month.
    """
    current_savings = 0.00
    for i in range(1,37):
        current_savings += current_savings * (0.04 / 12)
        current_savings += (rate/10000) * monthly_salary            # adding this months saved salary.
        if (i % 6 == 0):                                            # apply incremented salary after the 6th months saving as you will get updated salary on 7th month onwards.
            monthly_salary += semi_annual_raise * monthly_salary
    return current_savings


# bisection search
""" 
    This algorithm can also be implemented in this way. 
    but it only works if the target value function is strictly increasing or decreasing.
"""

# out of bounds for the given ip
#if(calculateSavings(end_rate , semi_annual_raise, monthly_salary) < portion_downpayment):
#    print("Not possible with this salary")

#else :
    # first bisection
guess = (start_rate + end_rate) / 2

# continue to bisect
while (abs(calculateSavings(guess, semi_annual_raise, monthly_salary) - portion_downpayment) > 100):
    bisection_count += 1
    if (bisection_count == 1 and calculateSavings(end_rate, semi_annual_raise, monthly_salary) < portion_downpayment):        
        print("Not possible with this salary")
        break
    else:
        if (calculateSavings(guess, semi_annual_raise, monthly_salary) > portion_downpayment):
            end_rate = guess
        else:
            start_rate = guess
        guess = (start_rate + end_rate) / 2
        print("bisection is", guess / 10000)
print("Optimum rate is:",guess / 10000)
print("Bisection Count is:", bisection_count)