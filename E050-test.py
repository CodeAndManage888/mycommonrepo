#**************************************************************
# Date: 053023   (Expected Solution with 24 Lines of Code)    *
# Title: Roots of a Quadratic Function                        *
# Status: In Progress (In Progress / Testing / Working)       *
# A univariate quadratic function has the form                *
# f(x) = ax^2 + bx +c, where a, b and c are constants, and a  *
# is non-zero. The roots of a quadratic function can be found *
# by finding the values of x that satisfy the quadratic       *
# equation ax^2 + bx + c =0. A quadratic function may have 0, *
# 1, or 2 real roots. These roots can be computed using the   *
# quadratic formula, shown below:                             *
#                                                             *
#                  -b +/- (b^2 - 4ac)^(1/2)                   *
#           root = -------------------------                  *
#                             2a                              *
#                                                             *
# The portion of the expression under the square root sign is *
# called the discriminant. If the discriminant is negative    *
# then the quadratic equation does not have any real roots.   *
# If the discriminant is 0, then the equation has one real    *
# root. Otherwise the equation has two real roots, and the    *
# expression must be evaluated twice, once using a plus sign, *
# and once using a minus sign, when computing the numerator.  *
#                                                             *
# Write a program that computes the real roots of a           *
# quadratic function. Your program should begin by prompting  *
# the user for the values of a, b, and c. Then it should      *
# display a message indicating the number of real roots,      *
# along with the values of the real roots (if any).           *
#                                                             *
# Computed Result Validated:                                  *
#**************************************************************
import math
#--------------------------------------------------------------
icheck = -1
no_spaces = " "
const_list = []
const_a, const_b, const_c, cUserIn1 = (0, 0, 0, 0)
pCombIn = 0
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
def discriminant(a, b, c):
  d = b**2 - 4*a*c
  if d < 0:
    r = 0
    fin_d = 0
  elif d == 0:
    r = 1
    fin_d = 0
  else:
    r = 2
    fin_d = math.sqrt(d)
  return r, fin_d
#--------------------------------------------------------------
i3Const = input("What are the values of a, b, and c constants e.g. 1, 3, 4? ==> ")
no_spaces = i3Const.replace(" ","")
pCombIn = data_check(no_spaces)
if (icheck == 0):
  const_list = i3Const.split()
  if len(const_list) == 3:
    const_a, const_b, const_c = [int(const) for const in const_list]
    if (const_a != 0) and (const_b != 0) and (const_c != 0):
      root, disc = discriminant(const_a, const_b, const_c)
      if root == 0:
#        fin_val1 = (-const_b + disc) / 2*const_a
#        fin_val2 = (-const_b - disc) / 2*const_a
        print("No real roots.")
      elif root == 1:
        fin_val1 = -const_b / 2*const_a
        print("One real root with the root values as %s only." % fin_val1)
      else:
        fin_val1 = (-const_b + disc) / 2*const_a
        fin_val2 = (-const_b - disc) / 2*const_a
        print("Two real roots with the root values as %s and %s." % (fin_val1, fin_val2))
    else:
      print("Invalid input data! Please use a non zero data.")
  else:
    print("Incomplete number of constants. Three sides are required.")
#--------------------------------------------------------------
print("Thank you for using this app.")
#**************************************************************