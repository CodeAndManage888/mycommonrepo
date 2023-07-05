#!/bin/bash
#**************************************************************
# Date: 063023   (Expected Solution with 22 Lines of Code)    *
# Title: No More Pennies                                      *
# Status: Testing (In Progress / Testing / Working)           *
# February 4, 2013 was the last day that pennies were         *
# distributed by the Royal Canadian Mint. Now that pennies    *
# have been phased out retailers must adjust totals so that   *
# they are multiples of 5 cents when they are paid for with   *
# cash (credit card and debit card transations continue to be *
# chared to the penny). While retailers have some freedom in  *
# how they do this, most choose to round to the closes nickel.*
#                                                             *
# Write a program that reads prices from the user until a     *
# blank line is entered. Display the total cost of all the    *
# entered items on one line, followed by the amount due if    *
# the customer pays with cash on a second line. The amount    *
# due for a cash payment should be rounded to the nearest     *
# nickel. One way to compute the cash payment amount is to    *
# begin by determining how many pennies would be needed to    *
# pay the total. Then compute the remainder when this number  *
# of pennies is divided by 5. Finally, adjust the total down  *
# if the reminder is less tha 2.5. Otherwise adjust the total *
# up.                                                         *
#                                                             *
# Computed Result Validated:                                  *
#**************************************************************
cost_list = []
num_cost_list = []
combcost, costcheck, icheck, ptr, total_cost = ("", 0, -1, 0, 0)
#--------------------------------------------------------------
def data_check(UserIn1):
  global icheck
  try:
    cUserIn1 = float(UserIn1)
    icheck = 0
    return cUserIn1
  except:
    icheck = -1
    print("Invalid input data! Numeric input data only.")
#--------------------------------------------------------------
InputCost = 1
while InputCost != " ":
  InputCost =input("Input price for the purchased item: ")
  cost_list.append(InputCost)

while cost_list[ptr] != " ":
  num_cost_list.append(data_check(cost_list[ptr]))
  ptr = ptr + 1
  if icheck == -1:
    break

if icheck == 0:
  for cost in num_cost_list:
    total_cost = total_cost + cost
  TotPen = total_cost * 100
  LeftOver = TotPen % 5
  if LeftOver < 2.5:
    TotCostCash = round(total_cost, 1)
  else:
    TotCostCash = round(total_cost, 2)

print("--------------------------------------------------")
print("Total purchased cost is $ %s" % format(total_cost, "0.2f"))
print("Total purchased cost if cash payment is $ %s" %  format(TotCostCash, "0.2f"))
print("--------------------------------------------------")
print("Thank you for using this app.")
#**************************************************************