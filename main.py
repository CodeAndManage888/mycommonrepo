class Solution:
    def cPF(self, fB: list[int], n: int) -> bool:
        idx = 0
        slot_ctr = 0
        for idx, slots in enumerate(fB):
            #print(idx, slots)
            if idx + 1 <= len(fB) - 1 and idx + 2 <= len(fB) - 1:
                if slots == 0 and fB[idx+1]==0 and len(fB)-1 == idx+1:
                    slot_ctr += 1
                elif slots == 0 and fB[idx+1]==0:
                    slot_ctr += 1
                    print(slot_ctr)
                    if fB[idx + 2] == 0:
                        idx += 2 
                    else:
                        idx += 1
                else:
                    idx += 1
        return slot_ctr >= n
            
ans_list = Solution()
list1 = [[1,0,0,0,1], [1,0,0,0,1], [1,0,0,0,1,0,0], [1,0,0,0,0,1]]
num_list =[1, 2, 2, 2]

for i in range(len(list1)):
    print(ans_list.cPF(list1[i], num_list[i]))

#next solution is to scan the content of the list.