#!/bin/bash
#**************************************************************
# Date: 070823   (Expected Solution with 24 Lines of Code)    *
# Title: Approximate Pi                                       *
# Status: Testing (In Progress / Testing / Working)           *
# The value of π can be approximated by the following         *
# infinite series:                                            *
#                                                             *
# pi = 3+4/(2x3x4)-4/(4x5x6)+4/(6x7x8)-4/(8x9x10) + ...       *
#                                                             *
# Write a program that displays 15 approximations of π. The   *
# first approximation should make use of only the first term  *
# from the infinite series. Each additional approximation     *
# displayed by your program should include one more term in   *
# the series, making it a better approximation of π than any  *
# of the approximations displayed previously.                 *
#                                                             *
# Computed Result Validated:                                  *
#**************************************************************
approx_cnt = 1
#--------------------------------------------------------------
def term_calc(indata1):
  a, b, c, out1, ctr = (2, 3, 4, 3, 1)
  while ctr <= indata1:
    if ctr % 2 != 0:
      out1 = out1 + 4/(a*b*c)
    else:
      out1 = out1 - 4/(a*b*c)
    a, b, c = (a + 2, b + 2, c + 2)
    ctr = ctr + 1
  return out1
#--------------------------------------------------------------
while approx_cnt != 16:
  pi_value = term_calc(approx_cnt) 
  print(format(pi_value,'0.15f'))
  approx_cnt = approx_cnt + 1
print("Thank you for using this app.")
#**************************************************************