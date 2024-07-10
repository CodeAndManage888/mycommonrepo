class Solution:
    def cPF(self, fB: list[int], n: int) -> bool:
        idx = 0
        slot_ctr = 0
        while idx < len(fB)-1 or idx + 1 < len(fB)-1 or idx + 2 < len(fB)-1 :
            if fB[idx] == 0 and fB[idx+1] == 0 and fB[idx+2] == 0 or fB[idx] == 0 and fB[idx+1] == 0 and fB[idx+2] == 1 or fB[idx] == 1 and fB[idx+1] == 0 and fB[idx+2] == 0:
                print(fB[idx], fB[idx+1], fB[idx+2])
                slot_ctr += 1
                idx += 2
            else:
                idx += 1
        print(slot_ctr)
        return slot_ctr >= n

ans_list = Solution()
list1 = [0,0,1,0,1]
num = 1

print(ans_list.cPF(list1, num))