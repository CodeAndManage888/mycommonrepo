class Solution:
    def cPF(self, fB: list[int], n: int) -> bool:
        #slots = fB.count(0) % n
        #return slots % 2 == 0
        idx = 0
        while True:
            if fB[idx] == 0:
                if fB[idx+1] == 0:
                    return True
            



                
    
            
            
        if n == 0:
            return True
                

ans_list = Solution()
list1 = [1, 0, 0, 0, 0, 1]
num = 2

print(ans_list.cPF(list1, num))