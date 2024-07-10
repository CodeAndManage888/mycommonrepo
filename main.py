class Solution:
    def cPF(self, fB: list[int], n: int) -> bool:
        idx = 0
        slot_ctr = 0
        while idx < len(fB)-1 or idx + 1 < len(fB)-1 or idx + 2 < len(fB)-1 :
            if fB[idx] == 1 and fB[idx+1] == 0 and fB[idx+2] == 1:
                slot_ctr += 1
                idx += 3
            else:
                idx += 1
        return slot_ctr >= n

ans_list = Solution()
list1 = [1, 0, 0, 0, 0, 1]
num = 2

print(ans_list.cPF(list1, num))