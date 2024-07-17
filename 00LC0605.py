class Solution:
    def cPF(self, fB: list[int], n: int) -> bool:
        idx = 0
        slot_ctr = 0
        while idx < len(fB):
            if idx + 2 < len(fB):
                if fB[idx] == 0 and fB[idx+1] == 0 and fB[idx+2] == 0:
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
list1 = [[1,0,0,0,1], [1,0,0,0,1], [1,0,0,0,1,0,0], [1,0,0,0,0,1],[1,0,0,0,0,0,1],[0,0,1,0,1]]
ans_lst = ["True", "False", "True", "False","True","True"]
num_list =[1, 2, 2, 2, 2, 1]

for i in range(len(list1)):
    print(ans_list.cPF(list1[i], num_list[i]),"--",ans_lst[i])

#next solution is to scan the content of the list.