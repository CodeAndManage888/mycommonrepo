#!/bin/bash
#**************************************************************
# Date: 082224 (Expected Solution with 83 Lines of Code)      *
# Title: Element Sequences                                    *
# Status: Testing (In Progress / Testing / Working)           *
#  Another game that some people play with the names of       *
# chemical elements involves constructing a sequence of       *
# elements where each element in the sequence begins with the *
# last letter of its predecessor. For example, if a sequence  *
# begins with Hydrogen, then the next element must be an      *
# element that begins with N, such as Nickel. The element     *
# following Nickel must begin with L, such as Lithium. The    *
# element sequence that is constructed can not contain any    *
# duplicates. Write a program that reads the name of an       *
# element from the user. Your program should use a recursive  *
# function to find the longest sequence of elements that      *
# begins with the entered element. Then it should display the *
# sequence. Ensure that your program responds in a reasonable *
# way if the user does not enter a valid element name. Hint:  *
# It may take your program up to two minutes to find the      *
# longest sequence for some elements. As a result, you might  *
# want to use elements like Molybdenum and Magnesium as       *
# your first test cases. Each has a longest sequence that is  *
# only 8 elements long which your program should find in a    *
# fraction of a second.                                       *
#                                                             *
# Computed Result Validated:                                  *
#**************************************************************
element_list = ['Zinc', 'Arsenic', 'Gold', 'Lead', 'Fluorine', 
                'Chlorine', 'Manganese', 'Bromine', 'Iodine', 
                'Astatine', 'Tennessine', 'Bismuth', 'Nickel', 
                'Helium', 'Lithium', 'Beryllium', 'Sodium', 
                'Magnesium', 'Aluminum', 'Potassium', 'Calcium', 
                'Scandium', 'Titanium', 'Vanadium', 'Chromium', 
                'Gallium', 'Germanium', 'Selenium', 'Rubidium', 
                'Strontium', 'Yttrium', 'Zirconium', 'Niobium', 
                'Molybdenum', 'Technetium', 'Ruthenium', 'Rhodium', 
                'Palladium', 'Cadmium', 'Indium', 'Tellurium', 
                'Cesium', 'Barium', 'Lanthanum', 'Cerium', 
                'Praseodymium', 'Neodymium', 'Promethium', 'Samarium', 
                'Europium', 'Gadolinium', 'Terbium', 'Dysprosium', 
                'Holmium', 'Erbium', 'Thulium', 'Ytterbium', 'Lutetium', 
                'Hafnium', 'Tantalum', 'Rhenium', 'Osmium', 'Iridium', 
                'Platinum', 'Thallium', 'Polonium', 'Francium', 'Radium', 
                'Actinium', 'Thorium', 'Protactinium', 'Uranium', 
                'Neptunium', 'Plutonium', 'Americium', 'Curium', 
                'Berkelium', 'Californium', 'Einsteinium', 'Fermium', 
                'Mendelevium', 'Nobelium', 'Lawrencium', 'Rutherfordium', 
                'Dubnium', 'Seaborgium', 'Bohrium', 'Hassium', 'Meitnerium', 
                'Darmstadtium', 'Roentgenium', 'Copernicium', 'Nihonium', 
                'Flerovium', 'Moscovium', 'Livermorium', 'Hydrogen', 'Boron', 
                'Carbon', 'Nitrogen', 'Oxygen', 'Neon', 'Silicon', 'Argon', 
                'Iron', 'Krypton', 'Tin', 'Xenon', 'Tungsten', 'Radon', 
                'Oganesson', 'Sulfur', 'Copper', 'Silver', 'Phosphorus', 
                'Cobalt', 'Antimony', 'Mercury']
final_list = n Progress (In Progress / Testing / Working)       *
#  Another game that some pe[]
#--------------------------------------------------------------
def long_seq(user_in, flist):
  if user_in.capitalize() in element_list:
    flist.append(user_in)
    element_list.pop(element_list.index(user_in))
  for i in range(len(element_list)):
    #print(element_list[i])
    #print("Before Cond 1 Entered:", user_in[-1], element_list[i][0])
    if user_in[-1] == element_list[i][0].lower():
      print("Cond 1 Entered:", user_in[-1], element_list[i][0])
      flist.append(element_list[i])
      element_list.pop(i)
      long_seq(flist[-1], flist)
      break
  return flist
#--------------------------------------------------------------
if __name__ == "__main__":
  element_name = input("Enter an element name: ")
  if element_name.isalpha() and element_name.capitalize() in element_list:
    print("The longest sequence of elements that begins with", element_name, "is", long_seq(element_name, final_list))
  else:
    print("Invalid element name.")
  print("Thank you for using this app.")
#**************************************************************