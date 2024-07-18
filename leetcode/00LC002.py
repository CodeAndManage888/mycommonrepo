def check_number(number):
  idx1 = 0
  list_number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
  while idx1 < len(list_number):
    idx2 = idx1 + 1
    while idx2 < len(list_number):
      if number == list_number[idx1] + list_number[idx2]:
        return idx1, idx2
      else:
        idx2 += 1
        continue
    idx1 += 1
if __name__ == "__main__":
  target_number = input("Enter a number: ")
  check_number(int(target_number))
  print("Thank you for using this app.")