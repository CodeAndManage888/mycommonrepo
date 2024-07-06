#For two strings s and t, we say "t divides s" if and only if s = t + t + t + ... + t + t (i.e., t is concatenated with itself one or more times).
#Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2. two strings s and t, we say "t divides s" if and only if s = t + t + t + ... + t + t (i.e., t is concatenated with itself one or more times).
#Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.

class Solution:
  def gcd(a, b):
      while b:
          a, b = b, a % b
      return a

  def gcdOfStrings(self, str1: str, str2: str) -> str:
      len1, len2 = len(str1), len(str2)

      gcd_len = gcd(len1, len2)

      candidate = str1[:gcd_len]
      print(candidate)
      print(len1 // gcd_len)
      print(len2 // gcd_len)

      if candidate * (len1 // gcd_len) == str1 and candidate * (len2 // gcd_len) == str2:
          return candidate
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