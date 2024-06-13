def reverse_integer(user_in):
  val1 = 2147483647
  val2 = -2147483647
  conv_bin_org = bin(user_in)
  conv_bin_string = str(conv_bin_org[2:])
  conv_bin_new = '0b' + conv_bin_string[::-1]
  conv_bin_int = int(conv_bin_new)
  if conv_bin_int > val1 or conv_bin_int < val2 or conv_bin_int == val1 or conv_bin_int == val2:
    conv_bin_int = 0
  




  
  if conv_bin[::-1] > bin(val1) or conv_bin[::-1] < bin(val2) or conv_bin[::-1] == bin(val1) or conv_bin[::-1] == bin(val2):
    conv_bin[::-1]

  else:
    return 0

if __name__ == "__main__":
  signed_32bit_integer = input("Enter a signed 32 bit integer: ")
  print("The reverse of the input is:", reverse_integer(int(signed_32bit_integer)))
  print("Thank you for using this app.")