# ------------------------------------------------------------------------
# Given a linked list, determine if it has a cycle in it.
# Follow up: Can you solve it without using extra space?
# ------------------------------------------------------------------------



'''
# ------------------------------------------------------------------------
# Given an array of integers that is already sorted in ascending order, 
# find two numbers such that they add up to a specific target number.
# The function twoSum should return indices of the two numbers such that 
# they add up to the target, where index1 must be less than index2 are not
# zero-based.
# Note: You may assume that each input would have exactly one solution.
# Input: numbers={2, 7, 11, 15}, target=9 Outpu: [1,2]
# ------------------------------------------------------------------------
def twoSum(numbers, target):
    # Write your code here
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            if numbers[i] + numbers[j] == target:
                return [i+1, j+1]
    return []
# ------------------------------------------------------------------------
# The main function
# ------------------------------------------------------------------------
if __name__ == "__main__":
    # Read in a list of integers
    line = input().strip()
    numbers = [int(x) for x in line.split(',')]
    # Sort the input list
    numbers.sort()
    print(numbers)
    # Read in the target
    target = int(input())
    # Find the two numbers that add up to the target
    print(twoSum(numbers, target))
# ------------------------------------------------------------------------
'''