#import site
#print(site.getsitepackages())
#x = 1
#print(x == 1)
#user_input = " "
#proc_data_one = user_input.strip()
#print(ord("A"), ord("Z"), ord("a"), ord("z"), ord("0"), ord("9"))
#digit_list = [2, 4, 5, "A", "F", "B"]
#print(digit_list.sort())
def fib1(n: int) -> int:
  if n < 2:
    return n
  else:
    return fib1(n - 1) + fib1(n - 2)
if __name__ == "__main__":
  print(fib1(5))