  def reverse_integer(user_in):
    val1 = "01111111111111111111111111111111"
    if user_in[::-1] == user_in:
      return user_in[::-1]
    else:
      return 0

  if __name__ == "__main__":
    signed_32bit_integer = input("Enter a signed 32 bit integer: ")
    print("The reverse of the input is:", reverse_integer(signed_32bit_integer))
    print("Thank you for using this app.")