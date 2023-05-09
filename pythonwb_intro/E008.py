#**************************************************************
# Date: 040321                                                *
# Gadgets n Gizmo                                             *
# Programmer: BoredManager                                    *
# An online retailer sells two products: widgets and gizmos.  *
# Each widget weighs 75 grams. Each gizmo weighs 112 grams.   *
# Write a program that reads the number of widgets and the    *
# number of gizmos in an order from the user. Then your       *
# program should compute and display the total weight of the  *
# order.                                                      *
#**************************************************************
computed_value = 0
icheck = -1
while icheck == -1:
    iWidget = input("Total order of widget/s from the customer ==> ")
    try:
        ciWidget = int(iWidget) # if an input "1.0" was used can this be accepted? (Q1)
        icheck = 0
    except:
        print("Please use whole number only.")
#--------------------------------------------------------------
icheck = -1
while icheck == -1:
    iGizmo = input("Total order of gizmo/s from the customer ==> ")
    try:
        ciGizmo = int(iGizmo)
        icheck = 0
    except:
        print("Please use whole number only.")
#--------------------------------------------------------------
cWidgetWt = 75
cGizmoWt = 112
computed_value = (ciWidget * cWidgetWt) + (ciGizmo * cGizmoWt)
#--------------------------------------------------------------
print("The total weight of %.f widget/s and %.f gizmo/s is %.f grams."\
% (ciWidget, ciGizmo, computed_value))
print("Thank you for using this app.")
#**************************************************************
# what have I learned from this challenge?
# - the challenge is not a big difference with the bottle deposit 
#   challenge. I actually rehash the program for that but added 
#   some improvement on the diplay process since i learned 
#   something new yesterday.
# - in using the display syntax i learned so far that there 
#   are 3 ways to put together a message. the use of a comma but 
#   it will at a space. the use of the "+" sign to concatenate 
#   the message then the use of some sort of a substitution 
#   syntax but not yet fully aware of it use. i think i am just 
#   barely scratching the surface. This one needs further 
#   reading (R1).
# - one the use of % is more efficient since the later two ways 
#   will require conversion of numbers to string and not to mention 
#   the use of round off syntax to format the output.
# - i also learned the use of continuation syntax "\". just make 
#   sure that there are no spaces between the last syntax and 
#   the next line i believe i should be alright. Although i 
#   need to read up more if there are other things that I 
#   should know about it(R2).
# - i am really appreciating how powerful the VS code editor 
#   is. I know that i am a beginner and i probably not used it 
#   to its full potential of what it can do but speaking from my 
#   experience in coding a COBOL program this is a huge improvement 
#   especially if you spent almost 12 years coding at a native 
#   mainframe environment.