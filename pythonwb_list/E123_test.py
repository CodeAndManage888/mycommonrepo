#!/bin/bash
#**************************************************************
# Date: 112423 (Expected Solution with 62 Lines of Code)      *
# Title: Infix to Postfix                                     *
# Status: Testing (In Progress / Testing / Working)           *
# Mathematical expressions are often written in infix form,   *
# where operators appear between the operands on which they   *
# act. While this is a common form, it is also possible to    *
# express mathematical expressions into postfix form, where   *
# the operator appears after both operands. For example, the  *
# infix expression 3 + 4 is written as 3 4 + in postﬁx form.  *
# One can convert an infix expression to postfix form using   * 
# the following algorithm:                                    *
#                                                             *
# Create a new empty list, operators                          *
# Create a new empty list, postfix                            *
#                                                             *
# For each token in the infix expression                      *
#    If the token is an integer then                          *
#       Add the token to the end of postfix.                  *
#    If the token is an operator then                         *
#       While operators is not empty and                      *
#             the last item in operators is not an open       *
#             parenthesis and precedence(token) < precedence  *
#             (last item in operators) do                     *
#         Remove the last item from operators and add it to   *
#         postﬁx                                              *
#       Add token to the end of operators                     *
#    If the token is an open parenthesis then                 *
#        Add token to the end of operators                    *
#    If the token is a close parenthesis then                 *
#       While the last item in operators is not an open       *
#       parenthesis do                                        *
#         Remove the last item from operators and add it to   *
#         postﬁx                                              *
#       Remove the open parenthesis from operators            *
#                                                             *
# While operators is not the empty list do                    *
#   Remove the last item from operators and add it to postﬁx  * 
#                                                             *
# Return postﬁx as the result of the algorithm                *
#                                                             *
# Use your solution to Exercise 122 to tokenize a mathematical*
# expression. Then use algorithm above to transform the       *
# expression from inﬁx form to postﬁx form. Your code that    *
# implements the preceding algorithm algorithm should reside  *
# in a function that takes a list of tokens representing an   *
# inﬁx expression as its only parameter. It should return a   *
# list of tokens representing the equivalent postﬁx expression*
# as its only result. Include a main program that demonstrates*
# your inﬁx to postﬁx function by reading an expression from  *
# the user in inﬁx form and displaying it in postﬁx form.     *
# The purpose of converting from inﬁx form to postﬁx form will*
# become apparent when you read Exercise 124. You may ﬁnd your*
# solutions to Exercises 90 and 91 helpful when completing    *
# this problem.                                               *
#                                                             *
# The algorithms provided in Exercises 123 and 124 do not     *
# perform any error checking. As a result, you may crash your *
# program or receive incorrect results if you provide them    *
# with invalid input. These algorithms can be extended to     *
# detect invalid input and respond to it in a reasonable      *
# manner. Doing so is left as an independent study exercise   *
# for the interested student.                                 *
#                                                             *
# Computed Result Validated:                                  *
#**************************************************************
symbol = ["*", "/", "(", ")" , "+", "-"]
#symbol2 = ["/", "+", "-"]
#--------------------------------------------------------------
def token_func(math_str):
  token_list = []
  no_spaces_list = math_str.split()
  print("Input: ", no_spaces_list)
  for exp in no_spaces_list:
    if len(exp) == 1:
      token_list.append(exp)
    else:
      signed_char = ""
      for char in exp:
        if char in symbol:
          if len(signed_char) != 0:
            token_list.append(signed_char)
            signed_char = ""
          token_list.append(char)
        elif char == "+" or char == "-" or char.isdigit():
          signed_char += char
      if signed_char != "":
        token_list.append(signed_char) 
  return token_list

def conv_infix_to_postfix(token_list):
  operators = []
  postfix = []
  close_open = []
  for token in token_list:
    if token.isdigit():
      postfix.append(token)
    elif token == "+" or token == "-" or token == "*" or token == "/":
      operators.append(token)
      close_open.clear()  #will clear the list
    elif token == "(":
      close_open.append(token)
      while operators != [] and operators[-1] == ")":
        postfix.append(operators.pop())
      if close_open[0] == ")" and close_open[1] == "(":
        operators.append("*")
      close_open.clear()  #will clear the list
    elif token == ")":
      close_open.append(token)
      while operators != [] and operators[-1] != "(":
        postfix.append(operators.pop())
  print("Not Empty: ", operators)
  #clean up steps?
  for item in operators:
    if item != "(" or item != ")":
      postfix.append(operators.pop())
    else:
      operators.pop()
  print("Empty: ", operators)
  return postfix
#--------------------------------------------------------------
if __name__ == "__main__":
  math_exp = input("Enter a mathematical expression w/ Spaces: ")
  infix_terms = token_func(math_exp)
  print("Infix: ", infix_terms)
  postfix_terms = conv_infix_to_postfix(infix_terms)
  print("Postfix: ", postfix_terms)
  print("Thank you for using this app.")
#**************************************************************
# Open Issues:
# 1.) The exercise 122 solution can't handle signed number that
#     affects the exercise 123 solution.