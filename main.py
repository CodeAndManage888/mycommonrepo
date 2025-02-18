#!/bin/bash
#**************************************************************
# Date: 080324 (Expected Solution with 41 Lines of Code)      *
# Title: Possible Change                                      *
# Status: In Progress (In Progress / Testing / Working)       *
#  Create a program that determines whether or not it is      *
# possible to construct a particular total using a specific   *
# number of coins. For example, it is possible to have a      *
# total of $1.00 using four coins if they are all quarters.   *
# However, there is no way to have a total of $1.00 using 5   *
# coins. Yet it is possible to have $1.00 using 6 coins by    *
# using 3 quarters, 2 dimes and a nickel. Similarly, a total  *
# of $1.25 can be formed using 5 coins or 8 coins, but a      *
# total of $1.25 can not be formed using 4, 6 or 7 coins.     *
# Your program should read both the dollar amount and the     *
# number of coins from the user. It should display a clear    *
# message indicating whether or not the entered dollar amount *
# can be formed using the number of coins indicated. Assume   *
# the existence of quarters, dimes, nickels and pennies when  *
# completing this problem. Your solution must use recursion.  *
# It can not contain any loops.                               *
#                                                             *
# Computed Result Validated:                                  *
#**************************************************************
#--------------------------------------------------------------
def coin_count(data1, data2, data3):
  data1 -= 25
  print("current count:", data1)
  data3 += 1
  if data3 != data2:
    print(data3)
    return coin_count(data1,data2,data3)
  else:
    print(data3)
    return data3
#--------------------------------------------------------------
if __name__ == "__main__":
  user_in1 = float(input("Enter the dollar amount: "))
  user_in2 = float(input("Enter the number of coins: "))
  ctr = 0
  total_coin = coin_count(user_in1*100,user_in2,ctr)
  print("total coins: ",total_coin, "expected coins: ",user_in2)
  if total_coin == user_in2:
    print("It is possible to have a total of $" +str(user_in1) + " using " + str(user_in2) + " coins.")
  else:
    print("It is not possible to have a total of $" + str(user_in1) + " using " + str(user_in2) + " coins.")
  print("Thank you for using this app.")
#**************************************************************