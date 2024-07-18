class Solution:
    def rvWrd(self, s: str) -> str:
        cnv_lst = []

        for word in range(len(s)):
            if word != " ":
                cnv_lst.append(s[word])

        cnv_lst.reverse()

        return " ".join(cnv_lst)

ans_list = Solution()
list1 = ["the sky is blue, "  hello world  ", "a good   example"]
ans_lst = ["blue is sky the", "world hello", "example good a"]

for i in range(len(list1)):
    print(ans_list.rvWrd(list1[i]),"--",ans_lst[i])
