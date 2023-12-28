#!/bin/bash
#**************************************************************
# Date: 112423 (Expected Solution with 62 Lines of Code)      *
# Title: Infix to Postfix                                     *
# Status: In Progress (In Progress / Testing / Working)       *
# Mathematical expressions are often written in infix form,   *
# where operators appear between the operands on which they   *
# act. While this is a common form, it is also possible to    *
# express mathematical expressions in postfix form, where the *
# operator appears after both operands. For example, the infix*
# expression 3+4 is written as 34+ in postﬁx form. One can    *
# convert an infix expression to postfix form using the       *
# following algorithm: Create a new empty list, operators     *
# Create a new empty list, postfix For each token in the infix*
# expression. If the token is an integer then Add the token to*
# the end of postfix. If the token is an operator then While  *
# operators is not empty and the last item in operators is    *
# not an open parenthesis and precedence(token)               *
# precedence (last item in operators) do Remove the last item *
# from operators and add it to postﬁx Add token to the end of *
# operators Ifthe token is an open parenthesis then Add token *
# to the end of operators Ifthe token is a close parenthesis  *
# then While the last item in operators is not an open        *
# parenthesis do Remove the last item from operators and add  *
# it to postﬁx Remove the open parenthesis from operators     *
# While operators is not the empty list do Remove the last    *
# item from operators and add it to postﬁx Return postﬁx as   *
# the result of the algorithm Use your solution to Exercise   *
# 122 to tokenize a mathematical expression. Then use the     *
# algorithm above to transform the expression from inﬁx form  *
# to postﬁx form. Your code that implements the preceding     *
# algorithm should reside in a function that takes a list of  *
# tokens representing an inﬁx expression as its only          *
# parameter. It should return a list of tokens representing   *
# the equivalent postﬁx expression as its only result.        *
# Include a main program that demonstrates your inﬁx to       *
# postﬁx function by reading an expression from the user in   *
# inﬁx form and displaying it in postﬁx form. This copy       *
# belongs to 'acha04'58 5 List Exercises The purpose of       *
# converting from inﬁx form to postﬁx form will become        *
# apparent when you read Exercise 124. You may ﬁnd your       *
# solutions to Exercises 90 and 91 helpful when completing    *
# this problem. The algorithms provided in Exercises 123 and  *
# 124 do not perform any error checking. As a result, you may *
# crash your program or receive incorrect results if you      *
# provide them with invalid input. These algorithms can be    *
# extended to detect invalid input and respond to it in a     *
# reasonable manner. Doing so is left as an independent study *
# exercise for the interested student.                        *
#                                                             *
# Computed Result Validated:                                  *
#**************************************************************
#--------------------------------------------------------------
def func_name(user_in):
  return
#--------------------------------------------------------------
if __name__ == "__main__":
  print("Thank you for using this app.")
#**************************************************************
