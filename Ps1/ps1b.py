
# Take user inputs. kept seperate variables with _str as suffix for simplicity
annual_salary_str = input("Enter your annual salary: ")
portion_saved_str = input("Enter the percent of your salary to save, as a decimal: ")
total_cost_str = input("Enter the cost of your dream home: ")
semi_annual_raise_str = input("Enter the semi-annual raise, as a decimal: ")

# variables initialization 
annual_salary = float(annual_salary_str) 
portion_saved = float (portion_saved_str)
total_cost = float(total_cost_str) 
semi_annual_raise = float(semi_annual_raise_str)
# hardcoded according to ps
current_savings = 0.00
months_required = 0
# derived variables
monthly_salary = annual_salary / 12
portion_downpayment = 0.25 * total_cost                         # 25% downpayment specified in requirements

while (current_savings < portion_downpayment):
    # ----------------------------------------------------------------------------------------------
    # return of investment should be made before adding current months savings 
    # as the return is actually on the previous months savings.
    # so add last months return and current monts saved portion to find current value of savings
    # returns to be hardcoded as 4% according to requirement    
    # --------------------------------------------------------------------------------------------
    current_savings += current_savings * (0.04 / 12)
    months_required += 1
    current_savings += portion_saved * monthly_salary           # adding this months saved salary.
    if (months_required % 6 == 0):                              # apply incremented salary after the 6th months saving as you will get updated salary on 7th month onwards.
        monthly_salary += semi_annual_raise * monthly_salary
    # print(current_savings, monthly_salary)

print("Number of months:",months_required)


