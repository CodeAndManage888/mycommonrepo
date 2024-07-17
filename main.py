class Solution:
    def cPF(self, fB: list[int], n: int) -> bool:
        idx = 0
        slot_ctr = 0
        while idx < len(fB):
            if fB[idx] == 0:
                if idx == 0 and len(fB) > 1:
                    if fB[idx+1] == 0:
                        slot_ctr += 1
                        idx += 2
                    else:
                        idx += 1
                elif idx != 0 and idx != len(fB)-1:
                    if fB[idx-1] == 0 and fB[idx+1] == 0:
                        slot_ctr += 1
                        idx += 2
                    else:
                        idx += 1
                elif idx == len(fB)-1:
                    if fB[idx-1] == 0:
                        slot_ctr += 1
                        idx += 1
                    else:
                        idx += 1
                continue
            else:
                idx += 1
                continue
        return slot_ctr >= n
            
ans_list = Solution()
list1 = [[1,0,0,0,1],[1,0,0,0,1],[1,0,0,0,1,0,0],[1,0,0,0,0,1],[1,0,0,0,0,0,1],[0,0,1,0,1],[1,0],[0],[0,0,1,0],[0,1,0]]
ans_lst = ["True", "False", "True", "False", "True", "True", "False", "True", "False","False"]
num_list =[1, 2, 2, 2, 2, 1, 1, 1, 2, 1]

for i in range(len(list1)):
    print(ans_list.cPF(list1[i], num_list[i]),"--",ans_lst[i])

#next solution is to scan the content of the list.