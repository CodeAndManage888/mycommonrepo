class Solution:
    def rvVwl(self, s: str) -> str:
        VwL_list = ["a","e","i","o","u","A","E","I","O","U"]
        ext_lst = []
        cnv_lst = []

        for ltr in range(len(s)):
            if s[ltr] in VwL_list:
                ext_lst.append(s[ltr])
            cnv_lst.append(s[ltr])                         

        ext_lst.reverse()

        for ltr in range(len(cnv_lst)):
            if cnv_lst[ltr] in VwL_list:
                cnv_lst[ltr] = ext_lst[0]
                ext_lst.pop(0)

        return "".join(cnv_lst)              

ans_list = Solution()
list1 = ["hello", "leetcode"]
ans_lst = ["holle", "leotcede"]

for i in range(len(list1)):
    print(ans_list.rvVwl(list1[i]),"--",ans_lst[i])
