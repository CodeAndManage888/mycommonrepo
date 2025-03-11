#!/bin/bash
#**************************************************************
# Date: 080324 (Expected Solution with 41 Lines of Code)      *
# Title: Possible Change                                      *
# Status: Testing (In Progress / Testing / Working)           *
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
# Computed Result Validated:                                  *a
#**************************************************************
#--------------------------------------------------------------
  def can_make_amount(amount, num_coins, coin_types):
    # Base cases
    if amount == 0 and num_coins == 0:
        return True  # Exact match
    if amount < 0 or num_coins <= 0:
        return False  # Exceeded constraints

    # Recursive case: Try using each coin and see if a valid combination exists
    for coin in coin_types:
        if can_make_amount(amount - coin, num_coins - 1, coin_types):
            return True  # Found a valid combination

    return False  # No valid combination found


  def main():
    # Read user input
    dollar_amount = float(input("Enter the dollar amount (e.g., 1.25): "))
    num_coins = int(input("Enter the number of coins: "))

    # Convert dollar amount to cents to work with integers
    amount_in_cents = int(round(dollar_amount * 100))

    # Define available coin denominations in cents
    coin_types = [25, 10, 5, 1]  # Quarters, dimes, nickels, pennies

    # Check if it's possible to form the amount with the given number of coins
    if can_make_amount(amount_in_cents, num_coins, coin_types):
        print(f"Yes, it is possible to form ${dollar_amount:.2f} using {num_coins} coins.")
    else:
        print(f"No, it is not possible to form ${dollar_amount:.2f} using {num_coins} coins.")


  if __name__ == "__main__":
    main()
#**************************************************************