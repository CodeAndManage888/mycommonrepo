class Solution:
  def IncTrp(self, nums: list[int]) -> bool:
      idx = 0
      if len(nums) < 3:
          return False
      else:
          for idx in range(len(nums)):
              if idx + 2 <= len(nums) - 1:
                  if nums[idx] < nums[idx + 1] and nums[idx + 1] < nums[idx + 2]:
                      print(idx, ":", nums[idx], nums[idx + 1], nums[idx + 2])
                      return True
              else:
                  if idx + 1 <= len(nums) - 1:
                      if nums[idx] < nums[idx + 1] and nums[idx + 1] > nums[0]:
                          print(idx, ":", nums[idx], nums[idx + 1], nums[0])
                          return True
                  else:
                      if idx == len(nums) - 1:
                          print(idx, ":", nums[idx], nums[0], nums[1])
                          return bool(nums[idx] < nums[0] and nums[0] < nums[1])

#===================== Generated line of codes ==============================
'''         if len(nums) < 3:
                return False
            
            first = float('inf')
            second = float('inf')
            
            for num in nums:
                if num <= first:
                    first = num
                elif num <= second:
                    second = num
                else:
                    return True
            return False
'''
#===================== Generated line of codes ==============================

ans_list = Solution()
list1 = [[1,2,3,4,5], [5,4,3,2,1], [2,1,5,0,4,6], [20,100,10,12,5,13], [2,4,-2,-3]]
ans_lst = ["True", "False", "True", "True", "False"]

for i in range(len(list1)):
  print(ans_list.IncTrp(list1[i]), "--", ans_lst[i])