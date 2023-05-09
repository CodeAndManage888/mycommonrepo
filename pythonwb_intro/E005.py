#**************************************************************
# Date: 040121                                                *
# Bottle Deposits                                             *
# Programmer: BoredManager                                    *
# In many jurisdictions a small deposit is added to drink     *
# containers to encourage people to recycle them. In one      *
# particular jurisdiction, drink containers holding one liter *
# or less have a $0.10 deposit, and drink containers holding  *
# more than one liter have a $0.25 deposit.                   *
# Write a program that reads the number of containers of each *
# size from the user. Your program should continue by         *
# computing and displaying the refund that will be received   *
# for returning those containers. Format the output so that   *
# it includes a dollar sign and always displays exactly two   *
# decimal places.                                             *
#**************************************************************
computed_value = 0
icheck = -1
while icheck == -1:
    iLtEq1Ltr = input("Total number of container/s with less than or equal to 1 Liter capacity ==> ")
    try:
        ciLtEq1Ltr = int(iLtEq1Ltr)
        icheck = 0
    except:
        print("Please use whole number only.")
#--------------------------------------------------------------
icheck = -1
while icheck == -1:
    iGt1Ltr = input("Total number of container/s with greater than 1 Liter capacity ==> ")
    try:
        ciGt1Ltr = int(iGt1Ltr)
        icheck = 0
    except:
        print("Please use whole number only.")
#--------------------------------------------------------------
LtEq1LtrRefund = .10
Gt1LtrRefund = .25
computed_value = (ciLtEq1Ltr * LtEq1LtrRefund) + (ciGt1Ltr * Gt1LtrRefund)
computed_value = round(computed_value,2)
final_value = str(computed_value)
#--------------------------------------------------------------
print("The total bottle/s refund is $ "+final_value)
print("Thank you for using this app.")

#**************************************************************
# what have I learned from this challenge?
# - adding the round function will ensure that it will always 
#   have a 2 decimal places regardless if other checks are 
#   already in place.
# - it will now check every input for invalid date unlike the 
#   previous apps.
# - the round functions lets you round to the nearest decimal
#   depending on the parameter. if you did not indicate a place 
#   value it will just truncate it to the interger but sill 
#   leaves out the decimal point, why? (A1)
