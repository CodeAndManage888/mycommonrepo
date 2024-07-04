class Solution:
  def gcdOfStrings(self, str1: str, str2: str) -> str:
      ctr = 0
      fin_gcd = ""
      while str1[ctr:ctr+1] == str2[ctr:ctr+1]:
          fin_gcd += str1[ctr:ctr+1]
          ctr += 1
          if fin_gcd[0:1] == str1[ctr:ctr+1]:
              return fin_gcd
      return fin_gcd

GcDofStrings = Solution()

final_answer = GcDofStrings.gcdOfStrings("ABCABC","ABC")
print(final_answer)
final_answer = GcDofStrings.gcdOfStrings("ABABAB","ABAB")
print(final_answer)
final_answer = GcDofStrings.gcdOfStrings("LEET","CODE")
print(final_answer)
final_answer = GcDofStrings.gcdOfStrings("ABCDEF","ABC")
print(final_answer)