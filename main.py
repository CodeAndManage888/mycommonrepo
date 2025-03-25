#!/bin/bash
#**************************************************************
# Date: 082124 (Expected Solution with 68 Lines of Code)      *
# Title: Spelling with Element Symbols                        *
# Status: In Progress (In Progress / Testing / Working)       *
#  Each chemical element has a standard symbol that is one,   *
# two or three letters long. One game that some people like   *
# to play is to determine whether or not a word can be        *
# spelled using only element symbols. For example, silicon    *
# can be spelled using the symbols Si, Li, C, O and N.        *
# However, hydrogen can not be spelled with any combination   *
# of element symbols. Write a recursive function that         *
# determines whether or not a word can be spelled using only  *
# element symbols. Your function will take two parameters:    *
# the word that you are trying to spell and a list of the     *
# symbols that can be used. Your function will return two     *
# results: a Boolean value indicating whether or not a        *
# spelling was found, and the string of symbols used to       *
# achieve the spelling (or an empty string if no spelling     *
# exists). Your function should ignore capitalization when    *
# searching for a spelling. Create a program that uses your   *
# function to ﬁnd and display all of the element names that   *
# can be spelled using only element symbols. Display the      *
# names of the elements along with the sequences of           *
# symbols. For example, one line of your output will be:      *
# Silver can be spelled as SiLvEr Your program will use the   *
# elements data set, which can be downloaded from the         *
# author’s website. This data set includes the names and      *
# symbols of all 118 chemical elements.                       *
#                                                             *
# Computed Result Validated:                                  *
#**************************************************************
elem_syms = [
  "H", "He", "Li", "Be", "B", "C", "N", "O", "F", "Ne",
  "Na", "Mg", "Al", "Si", "P", "S", "Cl", "Ar", "K", "Ca",
  "Sc", "Ti", "V", "Cr", "Mn", "Fe", "Co", "Ni", "Cu", "Zn",
  "Ga", "Ge", "As", "Se", "Br", "Kr", "Rb", "Sr", "Y", "Zr",
  "Nb", "Mo", "Tc", "Ru", "Rh", "Pd", "Ag", "Cd", "In", "Sn",
  "Sb", "Te", "I", "Xe", "Cs", "Ba", "La", "Ce", "Pr", "Nd",
  "Pm", "Sm", "Eu", "Gd", "Tb", "Dy", "Ho", "Er", "Tm", "Yb",
  "Lu", "Hf", "Ta", "W", "Re", "Os", "Ir", "Pt", "Au", "Hg",
  "Tl", "Pb", "Bi", "Po", "At", "Rn", "Fr", "Ra", "Ac", "Th",
  "Pa", "U", "Np", "Pu", "Am", "Cm", "Bk", "Cf", "Es", "Fm",
  "Md", "No", "Lr", "Rf", "Db", "Sg", "Bh", "Hs", "Mt", "Ds",
  "Rg", "Cn", "Nh", "Fl", "Mc", "Lv", "Ts", "Og"]
#--------------------------------------------------------------
def elem_check(word, elist):
  if len(word) == 0:
    return True
  else:
    for i in range(len(elist)):
      if word[0] == elist[i].lower() or word[:2].lower() == elist[i].lower():
        print(word[0], elist[i], word[:2])
        return elem_check(word[1:], elist)
    return False
#--------------------------------------------------------------
if __name__ == "__main__":
  check_word = input("Enter a word to check: ")
  check_word = check_word.lower()
  if elem_check(check_word.lower(), elem_syms):
    print("Word can be spelled using only element symbols.")
  else:
    print("Word cannot be spelled using only element symbols.")
  print("Thank you for using this app.")
#**************************************************************