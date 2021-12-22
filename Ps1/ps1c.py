#test commit to repo
#test changes from repo
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
optimal_rate = 0
start_rate = 0
end_rate = 10000
previous_end_rate = 10000


# func calculateSavings
def calculateSavings(rate,semi_annual_raise,monthly_salary):
    """
        This function will calculate the savings at the end of 36 months for a given rate of savings, semi-annual raise and salary.
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
    - begin with rates as 0 and 1
    - bisect at average of 1 and 0.
    - calculate the savings achieved for both the rates and check if they are greater than required downpayment
    - XOR results of both comparisons. XOR will be true only if savings by one of the rate is greater than required downpayment and 
      savings by other rate is less than required downpayment, thereby proving that the optimal rate lies within the two 
      rates.
    - if XOR is false means that the optimal rate is in other bisection
    - in that case keep the endrate as it is and make the start rate equal to the end_rate before the bisection was made
    - if the XOR is false before the first bisection it means that required savings cannot be acquired in 36 months.
"""

if not ((calculateSavings(start_rate,semi_annual_raise,monthly_salary) > portion_downpayment) 
        ^ (calculateSavings(end_rate, semi_annual_raise, monthly_salary) > portion_downpayment)):
        print("Not possible with this salary")
else:
    while (abs(calculateSavings(end_rate,semi_annual_raise,monthly_salary) - portion_downpayment) > 100):
        if ((calculateSavings(start_rate,semi_annual_raise,monthly_salary) > portion_downpayment )
            ^ (calculateSavings(end_rate, semi_annual_raise, monthly_salary) > portion_downpayment)):
            previous_end_rate = end_rate
            end_rate = (start_rate + end_rate) / 2
        else:
            start_rate = previous_end_rate
    print("optimal rate:",end_rate / 10000)
    print("optimal rate 2:",start_rate / 10000)


