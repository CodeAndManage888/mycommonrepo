class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        ctr = 0
        fin_gcd = ""
        print(str1.count(str2))
        if str1.count(str2) > 1:
            return str2
        else:
            while str1[ctr:ctr+1] == str2[ctr:ctr+1]:
                #print("current:", fin_gcd)
                fin_gcd += str1[ctr:ctr+1]
                ctr += 1
                if fin_gcd[0:1] == str1[ctr:ctr+1]:
                    break
            print(ctr, len(fin_gcd))
            print(fin_gcd[0:])
            print(str1[ctr:ctr+len(fin_gcd)])
            if fin_gcd[0:] == str1[ctr:ctr+len(fin_gcd)]:
                return fin_gcd
            else:
                return ""

GcDofStrings = Solution()

final_answer = GcDofStrings.gcdOfStrings("ABCABC","ABC")
print(final_answer)
final_answer = GcDofStrings.gcdOfStrings("ABABAB","ABAB")
print(final_answer)
final_answer = GcDofStrings.gcdOfStrings("LEET","CODE")
print(final_answer)
final_answer = GcDofStrings.gcdOfStrings("ABCDEF","ABC")
print(final_answer)
final_answer = GcDofStrings.gcdOfStrings("ABABABAB","ABAB")
print(final_answer)