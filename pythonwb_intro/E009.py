#**************************************************************
# Date: 040321                                                *
# Compound Interest                                           *
# Programmer: BoredManager                                    *
# Pretend that you have just opened a new savings account     * 
# that earns 4 percent interest per year. The interest that   * 
# you earn is paid at the end of the year, and is added to    * 
# the balance of the savings account. Write a program that    * 
# begins by reading the amount of money deposited into the    * 
# account from the user. Then your program should compute and * 
# display the amount in the savings account after 1, 2, and 3 *
# years. Display each amount so that it is rounded to 2       *
# decimal places.                                             *
#**************************************************************
computed_value = 0
icheck = -1
while icheck == -1:
    iTotalSavings = input("Please enter the total deposited amount into the savings account (Php) ==> ")
    try:
        ciTotalSavings = float(iTotalSavings)
        icheck = 0
    except:
        print("Please use number data only.")
#--------------------------------------------------------------
AnnualInterest = .04
comp_savings_Yr1 = ciTotalSavings + (ciTotalSavings * AnnualInterest)
comp_savings_Yr2 = comp_savings_Yr1 + (comp_savings_Yr1 * AnnualInterest)
comp_savings_Yr3 = comp_savings_Yr2 + (comp_savings_Yr2 * AnnualInterest)
#--------------------------------------------------------------
print("*--------------------------------------------*")
print("|       ++ Savings Account Summary ++        |")
print("| Opening Savings Amount: Php %.2f         | " % ciTotalSavings)
print("| Total Savings Amount in Year 1: Php %.2f | " % comp_savings_Yr1)
print("| Total Savings Amount in Year 2: Php %.2f | " % comp_savings_Yr2)
print("| Total Savings Amount in Year 3: Php %.2f | " % comp_savings_Yr3)
print("*--------------------------------------------*")
print("Thank you for using this app.")

#**************************************************************
# what have I learned from this challenge?
# - the challenge is another variation of the previous exercise.
# - i guess the aim here is to ensure that the programmer know
#   how to handle different kinds of computations.