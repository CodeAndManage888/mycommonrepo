def chk_pal(user_in):
  if user_in == user_in[::-1]:
    return True
  else:
    return False

if __name__ == "__main__":
  input_integer = input("Enter a number: ")
  print("The number is a palindrome:", chk_pal(input_integer))
  print("Thank you for using this app.")