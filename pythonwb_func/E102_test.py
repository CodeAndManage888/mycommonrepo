#!/bin/bash
#**************************************************************
# Date: 090123 (Expected Solution with 83 Lines of Code)      *
# Title: Reduce Measures                                      *
# Status: Testing (In Progress / Testing / Working)       *
# Many recipe books still use cups, tablespoons and teaspoons *
# to describe the volumes of ingredients used when cooking or *
# baking. While such recipes are easy enough to follow if you *
# have the appropriate measuring cups and spoons, they can be *
# difﬁcult to double, triple or quadruple when cooking        *
# Christmas dinner for the entire extended family. For        *
# example, a recipe that calls for 4 tablespoons of an        *
# ingredient requires 16 tablespoons when quadrupled.         *
# However, 16 tablespoons would be better expressed (and      *
# easier to measure) as 1 cup. Write a function that          *
# expresses an imperial volume using the largest units pos-   *
# sible. The function will take the number of units as its    *
# ﬁrst parameter, and the unit of measure (cup, tablespoon or *
# teaspoon) as its second parameter. Return a string          *
# representing the measure using the largest possible units   *
# as the function’s only result. For example, if the function *
# is provided with parameters representing 59 teaspoons then  *
# it should return the string “1 cup, 3 tablespoons, 2        *
# teaspoons”. Hint: One cup is equivalent to 16 tablespoons.  *
# One tablespoon is equivalent to 3 teaspoons.                *
#                                                             *
# Computed Result Validated:                                  *
#**************************************************************
input_list = []
#--------------------------------------------------------------
def calc_measurement(user_in1, user_in2):
  val_measure3 = ["Cups", "Cup", "cups", "cup"]
  val_measure2 = ["Tablespoon", "Tablespoons", "tablespoon", "tablespoons"]
  val_measure1 = ["Teaspoon", "Teaspoons", "teaspoon", "teaspoons"]
  cup_val, tbl_val, tea_val = 0, 0, 0
  if user_in2 in val_measure1:
    cup_val, tbl_val = user_in1 // (16 * 3), user_in1 % (16 * 3)
    tbl_val, tea_val = tbl_val // 3, tbl_val % 3
  elif user_in2 in val_measure2:
    cup_val, tbl_val = user_in1 // 16, user_in1 % 16
    tbl_val, tea_val = tbl_val // 3, tbl_val % 3
  elif user_in2 in val_measure3:
    cup_val = user_in1
  else:
    print("Invalid Input Data")
  message = "%s Cup(s), %s Tablespoon(s), %s Teaspoon(s)" % (cup_val, tbl_val, tea_val)
  return message
#--------------------------------------------------------------
if __name__ == "__main__":
  user_input = input("Enter the unit and its measure e.g. 2 cups: ")
  input_list = user_input.split(" ")
  print(calc_measurement(int(input_list[0]), input_list[1]))
  print("Thank you for using this app.")
#**************************************************************