#**************************************************************
# Date: 061323   (Expected Solution with 44 Lines of Code)    *
# Title: Cell Phone Bill                                      *
# Status: Testing (In Progress / Testing / Working)           *
# A particular cell phone plan includes 50 minutes of air     *
# time and 50 text messages for $15.00 a month. Each          *
# additional minute of air time costs $0.25, while additional *
# text messages cost $0.15 each. All cell phone bills include *
# an additional charge of $0.44 to support 911 call centers,  *
# and the entire bill (including the 911 charge) is subject   *
# to 5 percent sales tax.                                     *
#                                                             *
# Write a program that read the number of minutes and text    *
# messages used in a month from the user. Display the base    *
# charge, additional minutes charge (if any), additional text *
# message charge (if any), the 911, tax and total bill amount.*
# Only display the additional minute and text message charges *
# if the user incurred costs in these categories. Ensure that *
# all of the charges are displayed using 2 decimal places.    *
#                                                             *
# Computed Result Validated:                                  *
#**************************************************************
icheck = -1
base_bill, charge_911, piNoMin, piNoMsg = (15.00, .44, 0, 0)
iNoMin, iNoMsg = (" ", " ")
comp_fin_bill, comp_piNoMin, comp_piNoMsg = (0, 0, 0)
#--------------------------------------------------------------
def data_check(UserIn1):
  global icheck
  try:
    cUserIn1 = int(UserIn1)
    icheck = 0
    return cUserIn1
  except:
    print("Invalid input data! Numeric input data only.")
#--------------------------------------------------------------
iNoMin = input("How many minutes consumed this month? Numeric only e.g. (1, 3, 4)==> ")
iNoMsg = input("How many messages consumed this month? Numeric only e.g. (1, 3, 4)==> ")
print(" ")
print("-----------------------------------------------------")
print("Billing Statement for this Month")
print("-----------------------------------------------------")
piNoMin = data_check(iNoMin)
if icheck == 0:
  piNoMsg = data_check(iNoMsg)
  if icheck == 0:
    print("Base Charge for this month is $%s" % format(base_bill, '0.2f'))
    print("911 Charge for this month is $%s" % format(charge_911, '0.2f'))
    if (piNoMin <= 50 or piNoMsg <= 50) and (piNoMsg != 0 and piNoMin != 0):
      comp_fin_bill = format (((15 + .44)*1.05), '0.2f')
      print("-----------------------------------------------------")
      print("Total Bill for this month with 5%% tax is $%s" % comp_fin_bill)
      print(" ")
    elif (piNoMin > 50 or piNoMsg > 50) and (piNoMsg != 0 and piNoMin != 0):
      if piNoMin > 50:
        comp_piNoMin = (piNoMin - 50)*.25
        if comp_piNoMin < 0:
          comp_piNoMin = 0.00
        print("Additional Charge due to extra Air Time for this month is $%s" % format(comp_piNoMin, '0.2f'))
      if piNoMsg > 50:
        comp_piNoMsg = (piNoMsg - 50)*.15
        if comp_piNoMsg < 0:
          comp_piNoMsg = 0.00
        print("Additional Charge due to extra Messages for this month is $%s" % format(comp_piNoMsg, '0.2f'))
      comp_fin_bill = format(((comp_piNoMin + comp_piNoMsg + 15 + .44)*1.05), '0.2f')
      print("-----------------------------------------------------")
      print("Total Bill for this month with 5%% tax is $%s" % comp_fin_bill)
      print(" ")
    else:
      print("Invalid input data! Please use a non zero data.")
#--------------------------------------------------------------
print("Thank you for using this app.")
#**************************************************************