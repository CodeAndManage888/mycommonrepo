
user_input = 0
while user_input == 0:
    user_input = input("Please give me a number: ")
    try:
        ival = 0
        istr = int(user_input)
    except:
        ival = -1
    if ival == -1:
        user_input = 0
        print("Invalid Input!")
    else:
        if istr == 0:
            print ("Data is Zero.")
        elif istr < 5:
            print ("Data is between 1 and 4.")
        elif istr > 5:
            print ("Data is greater than 5.")
        elif istr > 10:
            print ("Data is too big to handle.")