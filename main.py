#import site
#print(site.getsitepackages())
#x = 1
#print(x == 1)
#user_input = " "
#proc_data_one = user_input.strip()
#print(ord("A"), ord("Z"), ord("a"), ord("z"), ord("0"), ord("9"))
#digit_list = [2, 4, 5, "A", "F", "B"]
#print(digit_list.sort())
#count = len([ltr in ltr for ltr in "ABADZFAHIJKLMNOPQRSTUVWXYZ" if ltr == "A" and ltr == "Z"])
#def greet(name):
#'''This function greets the person passed in as a parameter'''
#print("Hello, " + name)
#-----------------------------------------------------------------------------------
#Algorithm 1: Fibonacci using Recurssion
#def fib1(n: int) -> int:
#  if n < 2:
#    print("condition 1")
#    return n
#  else:
#    print("condition 2")
#    return fib1(n - 1) + fib1(n - 2)
#if __name__ == "__main__":
#  user_num = int(input("Enter a number: "))
#  print(fib1(user_num))
#-----------------------------------------------------------------------------------
#Algorith 2: Fibonacci
def comp(n):
  for i in range(n):
    print(i, end="")
    print(i + (i+1), end="")
  return
if __name__ == "__main__":
  user_num = int(input("Enter a number: "))
  comp(user_num)