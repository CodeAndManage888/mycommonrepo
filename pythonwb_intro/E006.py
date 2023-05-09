#**************************************************************
# Date: 040221                                                *
# Tax and Tip                                                 *
# Programmer: BoredManager                                    *
# The program that you create for this exercise will begin by * 
# reading the cost of a meal ordered at a restaurant from the * 
# user. Then your program will compute the tax and tip for    * 
# the meal. Use your local tax rate when computing the amount * 
# of tax owing. Compute the tip as 18 percent of the meal     * 
# amount (without the tax). The output from your program      * 
# should include the tax amount, the tip amount, and the      * 
# grand total for the meal including both the tax and the     * 
# tip. Format the output so that all of the values are        * 
# displayed using two decimal places.                         *
#**************************************************************
computed_value = 0
icheck = -1
while icheck == -1:
    iMealCost = input("Please enter the total meal amount in Php ==> ")
    try:
        ciMealCost = float(iMealCost)
        icheck = 0
    except:
        print("Please use number data only.")
#--------------------------------------------------------------
PhpTax = .10
TipPercent = .18
computed_tax = round((ciMealCost * PhpTax),2)
computed_tip = round((ciMealCost * TipPercent),2)
total_computed_value = ciMealCost + computed_tax + computed_tip
total_computed_value = round(total_computed_value,2)
ciMealCost = round(ciMealCost,2)
#--------------------------------------------------------------
final_cost = str(ciMealCost)
final_tip = str(computed_tip)
final_tax = str(computed_tax)
final_value = str(total_computed_value)
#--------------------------------------------------------------
print("The meal amount is Php "+final_cost)
print("The tax amount is Php "+final_tax)
print("The tip amount is Php "+final_tip)
print("The total amount due is Php "+final_value)
print("Thank you for using this app.")

#**************************************************************
# what have I learned from this challenge?
# - it gets easier because the next challenge is usually a 
#   variation of the previous one.
# - i still need to brush up with the variable definition and 
#   available operation in Python (A1).