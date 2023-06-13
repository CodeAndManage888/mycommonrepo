#**************************************************************
# Date: 060123   (Expected Solution with 52 Lines of Code)    *
# Title: Letter Grade to Grade Points                         *
# Status: In Progress (In Progress / Testing / Working)       *
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
icheck = -1
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
#--------------------------------------------------------------
iLetterGrade = input("What is the letter grade(A+, A etc)?==> ")
if (i1stChar in notes_list) and (i2ndChar in notes_list):
  ci1stChar, ci2ndChar = (i1stChar.upper(), int(i2ndChar))
  mid_hz = note_hz_dict[ci1stChar]
  fin_hz = format(round((mid_hz / 2**(4 - ci2ndChar)), 2), '0.2f')
  print("The %s%s note has a frequency of %s Hz" % (ci1stChar, i2ndChar, fin_hz))
else:
  if len(iNameNotes) == 2:
    print("Invalid input data! Please use valid note name(C4, A0).")
  else:
    print("Invalid input data! Up to two charater data only.")
print("Thank you for using this app.")
#**************************************************************