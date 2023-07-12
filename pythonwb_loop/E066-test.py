#!/bin/bash
#**************************************************************
# Date: 070823   (Expected Solution with 62 Lines of Code)    *
# Title: Compute a Grade Point Average                        *
# Status: Testing (In Progress / Testing / Working)           *
# Exercise 51 included a table that shows the conversion from *
# letter grades to gradepoints at a particular academic       *
# institution. In this exercise you will compute the grade    *
# point average of an arbitrary number of letter grades       *
# entered by the user. The user will enter a blank line to    *
# indicate that all of the grades have been provided. For     *
# example, if the user enters A, followed by C+, followed by  *
# B, followed by a blank line then your program should report *
# a grade point average of 3.1.                               *
# You may find your solution to Exercise 51 helpful when      *
# completing this exercise.Your program does not need to do   *
# any error checking. It can assume that each value entered   *
# by the user will always be a valid letter grade or a blank  *
# line.                                                       *
#                                                             *
# Computed Result Validated:                                  *
#**************************************************************
LetterGradeDict = {"A+": 4.0, "A": 4.0, "A-": 3.7, "B+": 3.3,
                     "B": 3.0, "B-": 2.7, "C+": 2.3, "C": 2.0,
                     "C-": 1.7, "D+": 1.3, "D": 1.0, "F": 0.0}
val_let_grade_list=["A+", "a+", "A", "a", "A-", "a-", "B+", "b+", "B", "b", "B-",
            "b-", "C+", "c+", "C", "c", "C-", "c-", "D+", "d+", "D", "d","F","f"," "]
iLetterGrade, ciLetterGrade, SumGradePt, GradeCtr, ErrorFlag = ("", " ", 0.0, 0.0, 0)
#--------------------------------------------------------------
while iLetterGrade != " ":
  iLetterGrade = input("Enter the letter grade(A+, A etc)? ==> ")
  if iLetterGrade in val_let_grade_list:
    ciLetterGrade = iLetterGrade.upper()
    if iLetterGrade != " ":
      SumGradePt = SumGradePt + LetterGradeDict[ciLetterGrade]
      GradeCtr = GradeCtr + 1
  else:
    print("The %s letter grade is invalid." % iLetterGrade)
    ErrorFlag = 1
    break
if ErrorFlag == 0:
  GradePtAve = SumGradePt / GradeCtr
  print("The average of these letter grades is %s grade point(s)." % GradePtAve)
print("Thank you for using this app.")
#**************************************************************