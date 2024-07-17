class Solution:
    def cPF(self, fB: list[int], n: int) -> bool:
        idx = 0
        slot_ctr = 0
        while idx < len(fB):
            if len(fB) <= 3:
                if len(fB) == 3:
                    if fB[0] + fB[1] == 0 or sum(fB) == 0 or fB[1] + fB[2] == 0:
                        slot_ctr += 1
                        break
                    else:
                        break
                elif len(fB) == 2:
                    if fB[0] + fB[1] == 0 or sum(fB) == 0:
                        slot_ctr += 1
                        break
                    else:
                        break
                elif len(fB) == 1:
                    if fB[0] == 0:
                        slot_ctr += 1
                        break
                    else:
                        break
                else:
                    break
            elif idx + 2 < len(fB):
                if fB[idx] == 0 and fB[idx+1] == 0 and fB[idx+2] == 0 or idx == 0 and fB[idx] == 0 and fB[idx+1] == 0:
                    slot_ctr += 1
                    idx += 2
                else:
                    idx += 1
                    continue
            elif idx + 1 < len(fB):
                if fB[idx] == 0 and fB[idx+1] == 0:
                    slot_ctr += 1
                    idx += 1
                else:
                    idx += 1
                    continue
            elif idx < len(fB):
                if fB[idx] == 0:
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
list1 = [[1,0,0,0,1],[1,0,0,0,1],[1,0,0,0,1,0,0],[1,0,0,0,0,1],[1,0,0,0,0,0,1],[0,0,1,0,1],[1,0],[0],[0,0,1,0]]
ans_lst = ["True", "False", "True", "False", "True", "True", "False", "True", "False"]
num_list =[1, 2, 2, 2, 2, 1, 1, 1, 2]

for i in range(len(list1)):
    print(ans_list.cPF(list1[i], num_list[i]),"--",ans_lst[i])

#next solution is to scan the content of the list.