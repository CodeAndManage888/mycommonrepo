class Solution:
    def cPF(self, fB: list[int], n: int) -> bool:
        slots = fB.count(0) % n
        return slots % 2 == 0

ans_list = Solution()
list1 = [1, 0, 0, 0, 1]
num = 1

print(ans_list.cPF(list1, num))
