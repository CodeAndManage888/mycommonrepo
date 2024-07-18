class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        ans_list = []
        for candy in candies:
            if candy + extraCandies >= max(candies):
                ans_list.append(True)
            else:
                ans_list.append(False)
        return ans_list

ans_list = Solution()

candies = [2, 3, 5, 1, 3]
extraCandies = 3

print(ans_list.kidsWithCandies(candies, extraCandies))