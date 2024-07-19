class Solution:
  def mergeAlternately(self, word1: str, word2: str) -> str:
      ctr = 0
      comb_str = ""
      if len(word1) == len(word2) or len(word1) > len(word2):
          # process 1 here
          while ctr < len(word1):
              comb_str += word1[ctr:ctr+1] + word2[ctr:ctr+1]
              ctr += 1
          return comb_str
      elif len(word1) < len(word2):
          # process 2 here
          while ctr < len(word2):
              comb_str += word1[ctr:ctr+1] + word2[ctr:ctr+1]
              ctr += 1
          return comb_str

Answer = Solution()

MergedWord = Answer.mergeAlternately("abcd", "pq")
print(MergedWord)
MergedWord = Answer.mergeAlternately("abcd", "pqrs")
print(MergedWord)
MergedWord = Answer.mergeAlternately("ab", "pqrs")
print(MergedWord)