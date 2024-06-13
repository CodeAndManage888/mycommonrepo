def reverse_integer(user_in):
  val1 = 2147483647
  val2 = -2147483647
  conv_bin = bin(user_in)
  if conv_bin[::-1] > bin(val1) or conv_bin[::-1] < bin(val2) or conv_bin[::-1] == bin(val1) or conv_bin[::-1] == bin(val2):
    conv_bin[::-1]
    
  else:
    return 0

if __name__ == "__main__":
  signed_32bit_integer = input("Enter a signed 32 bit integer: ")
  print("The reverse of the input is:", reverse_integer(int(signed_32bit_integer)))
  print("Thank you for using this app.")