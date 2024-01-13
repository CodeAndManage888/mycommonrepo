#-----------------------------------------------------------------------------------
import array as arr
from array import *
special_nums = arr.array('d', [0.577, 1.618, 2.718, 3.14, 6, 37, 1729])
for i in special_nums:
  print(i)
'''
#-----------------------------------------------------------------------------------
def my_func(f, arg):
    return f(arg)

my_func(lambda x: 2*x*x, 5)
#-----------------------------------------------------------------------------------
def apply_twice(func, arg):
  return func(func(arg))

def add_five(x):
  return x + 

print(apply_twice(add_five, 10))
#-----------------------------------------------------------------------------------
def fibonacci(x: int) -> int:
  if x == 0:
    return 0
  elif x == 1:
    return 1
  else:
    return fibonacci(x-1) + fibonacci(x-2)
if __name__ == "__main__":
  x = int(input("Enter a number: "))
  ctr = 0
  while ctr < x:
    print(fibonacci(ctr))
    ctr += 1
#-----------------------------------------------------------------------------------
def febseq(x):
  if x == 0 or x == 1:
    return 1
  else:
    return febseq(x-1) + febseq(x-2)
print(febseq(10))
#-----------------------------------------------------------------------------------
def breakword():
  word = input("Enter a word: ")
  oltr = ""
  for ltr in word:
    oltr += ltr
    yield oltr

print(list(breakword()))
#-----------------------------------------------------------------------------------
triple = lambda x: x * 3
add = lambda x, y: x + y
print(add(triple(3), 4))
#-----------------------------------------------------------------------------------
def polynomial(x):
    return x**2 + 5*x + 4
print(polynomial(5))

print((lambda x: x**2 + 5*x + 4)(5))
#-----------------------------------------------------------------------------------
def my_func(f, arg):
  return f(arg)

x = int(input())

print(my_func(lambda x: 2*x*x, x))
#-----------------------------------------------------------------------------------
txt = input("Enter a string: ")
word_list = txt.split()
long_word = ""
for word in word_list:
  if len(word) >= len(long_word):
    long_word = word
print(long_word)
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
'''
'''
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
#def comp(n):
#  for i in range(n):
#    if i < 2:
#      print(i)
#    else:
#      print(i+1)
#  return
#if __name__ == "__main__":
#  user_num = int(input("Enter a number: "))
#  comp(user_num)
#-----------------------------------------------------------------------------------
#price = {"Nachos":6, "Pizza":6, "Cheeseburger":10, "Water":4, "Coke":5}
#olist = []
#tax = .07
#total = 0

#order = input()
#olist = order.split()
#for o in olist:
#    total += price.get(o,5)
#total += total*tax
#f_total = f"{total:.2f}"
#print(f_total)
#-----------------------------------------------------------------------------------
def add(x,y):
  print(add(x + y,x*y))
  return
func = add
func(1,2)
test run
#-----------------------------------------------------------------------------------
pyfile = open("00E122.py", "r")
for num in range(0,100):
  print(pyfile.read(5))
pyfile.close()
#-----------------------------------------------------------------------------------
with open("00E122.py", "r") as code:
  for num in range(0,10):
    print(code.read(5))
#-----------------------------------------------------------------------------------
squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(squares[1:-1])
'''