#!/bin/bash
#**************************************************************
# Date: 112423 (Expected Solution with 58 Lines of Code)      *
# Title: Evaluate Postﬁx                                      *
# Status: In Progress (In Progress / Testing / Working)       *
# Evaluating a postﬁx expression is easier than evaluating an *
# inﬁx expression because it does not contain any brackets    *
# and there are no operator precedence rules to consider. A   *
# postﬁx expression can be evaluated using the following      *
# algorithm: Create a new empty list, values Foreach token in *
# the postﬁx expression Ifthe token is a number then Convert  *
# it to an integer and add it to the end of values Else       *
# Remove an item from the end of values and call it right     *
# Remove an item from the end of values and call it left      *
# Apply the operator to leftandright Append the result to the *
# end of values Return the ﬁrst item in values as the value   *
# of the expression Write a program that reads a mathematical *
# expression in inﬁx form from the user, evaluates it, and    *
# displays its value. Uses your solutions to Exercises 122    *
# and 123 along with the algorithm shown above to solve this  *
# problem.                                                    *
#                                                             *
# Computed Result Validated:                                  *
#**************************************************************
#--------------------------------------------------------------
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