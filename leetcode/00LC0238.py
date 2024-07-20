class Solution:
  def pEs(self, nums: list[int]) -> list[int]:
      new_list, prod, temp_list = [], 0, []
      for idx, num in enumerate(nums):
          temp_list = nums.copy()
          temp_list.pop(idx)
          for idx2, num2 in enumerate(temp_list):
              if idx2 == 0:
                  prod = num2
              else:
                  prod *= num2
          new_list.append(prod)
      return new_list

ans_list = Solution()
list1 = [[1,2,3,4],[-1,1,0,-3,3]]
ans_lst = [[24,12,8,6], [0,0,9,0,0]]

for i in range(len(list1)):
    print(ans_list.pEs(list1[i]),"--",ans_lst[i])

#=========================== Generated Answer ============================
class Solution:
  def pEs(self, nums: list[int]) -> list[int]:
    length = len(nums)
    answer = [1] * length

    # Step 1: Calculate prefix products and store them in answer
    prefix_product = 1
    for i in range(length):
        answer[i] = prefix_product
        prefix_product *= nums[i]

    # Step 2: Calculate suffix products and multiply with the prefix products in answer
    suffix_product = 1
    for i in range(length - 1, -1, -1):
        answer[i] *= suffix_product
        suffix_product *= nums[i]

    return answer