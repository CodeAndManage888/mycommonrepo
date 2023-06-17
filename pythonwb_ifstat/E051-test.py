#**************************************************************
# Date: 060123   (Expected Solution with 52 Lines of Code)    *
# Title: Letter Grade to Grade Points                         *
# Status: Testing (In Progress / Testing / Working)           *
# At a particular university, letter grades are mapped to     *
# grade points in the following manner:                       *
#                                                             *
# Letter                  Grade Points                        *
# --------                ---------------                     *
# A+                      4.0                                 *
# A                       4.0                                 *
# A-                      3.7                                 *
# B+                      3.3                                 *
# B                       3.0                                 *
# B-                      2.7                                 *
# C+                      2.3                                 *
# C                       2.0                                 *
# C-                      1.7                                 *
# D+                      1.3                                 *
# D                       1.0                                 *
# F                       0.0                                 *
#                                                             *
# Write a program that begins by reading a letter grade from  *
# the user. Then your program should compute and display the  *
# equivalent number of grade points. Ensure that your program *
# generates an appropriate error message if the user enters   *
# an invalid letter grade.                                    *
#                                                             *
# Computed Result Validated:                                  *
#**************************************************************
letter_grade_dict = {
   "A+": 4.0,
    "A": 4.0,
   "A-": 3.7,
   "B+": 3.3,
    "B": 3.0,
   "B-": 2.7,
   "C+": 2.3,
    "C": 2.0,
   "C-": 1.7,
   "D+": 1.3,
    "D": 1.0,
    "F": 0.0
}
val_let_grade_list=["A+", "a+", "A", "a", "A-", "a-", "B+", "b+", "B", "b", "B-",
            "b-", "C+", "c+", "C", "c", "C-", "c-", "D+", "d+", "D", "d","F","f"]
iLetterGrade, ciLetterGrade, fin_grade = (" ", " ", 0)
#--------------------------------------------------------------
iLetterGrade = input("What is the letter grade(A+, A etc)?==> ")
if iLetterGrade in val_let_grade_list:
  ciLetterGrade = iLetterGrade.upper()
  fin_grade = letter_grade_dict[ciLetterGrade]
  print("The %s letter grade is equivalent to %s grade point(s)." % (ciLetterGrade, fin_grade))
else:
  print("The %s letter grade is invalid." % iLetterGrade)
print("Thank you for using this app.")
#**************************************************************