#**************************************************************
# Date: 052423   (Expected Solution with 39 Lines of Code)    *
# Title: Note to Frequency                                    *
# Status: In Progress (In Progress / Testing / Working)       *
# The following table lists an octave of music notes,         *
# beginning with middle C, along with their frquencies.       *
# Note              Frequency (Hz)                            *
# C4                261.63                                    *
# D4                293.66                                    *
# E4                329.63                                    *
# F4                349.23                                    *
# G4                392.00                                    *
# A4                440.00                                    *
# B4                493.88                                    *
#                                                             *
# Begin by writing a program that reads the name of a note    *
# from the user and displays the note's frequency. Your       *
# program should support all of the notes listed previously.  *
#                                                             *
# Once you have your program working correctly for the notes  *
# listed previously you should sigeport for all of the     *
# notes from C0 to C8. While this could be done by adding     *
# many additional cases to your if statement, such a solution *
# is cumbersome, inelegant and unacceptable for the purposes  *
# of this exercise. Instead you should exploit the            *
# relationship between notes in adjacent octaves. in          *
# particular, the frequency of any note in octave N is half   *
# the frequency of the corresponding note in octave N + 1. By *
# using the relationship. you should be able to add support   *
# for the additional notes without adding additional cases to *
# your if statement.                                          *
#                                                             *
# Hint: To complete this exercise you will need to extract    *
# individual characters from the two-character note name so   *
# that you can work with the letter and the octave number     *
# separately. Once you have separated the parts, compute the  *
# frequency of the note in the fourth octave using the data   *
# in the table above. Then divide the frequency by 2^(4-x),   *
# where x is the octave number entered by the user. This will *
# have or double the frequency the correct number of times.   *
#                                                             *
# Computed Result Validated:                                  *
#                                                             *
#**************************************************************
icheck = -1
mid_hz, fin_hz = (0, " ")
i1stChar, i2ndChar, ci1stChar, ci2ndChar = (" ", " ", " ", 0)
note_hz_dict = {
   "C": 261.63,
   "D": 293.66,
   "E": 329.63,
   "F": 349.23,
   "G": 392.00,
   "A": 440.00,
   "B": 493.88
}
notes_list=["c", "d", "e", "f", "g", "a", "b", "C", "D", "E", "F",
            "G", "A", "B", "0", "1", "2", "3", "4", "5", "6", "7",
            "8"]
#--------------------------------------------------------------
iNameNotes = input("What is the name of the note(C4, A0 etc)?==> ")
i1stChar, i2ndChar = (iNameNotes[0], iNameNotes[1])
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
# Open Items:
#
# CHistory:
# C0525231200
# - complete the code and ready for testing