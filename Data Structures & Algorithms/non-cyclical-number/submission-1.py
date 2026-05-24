class Solution:
    def isHappy(self, n: int) -> bool:
        
        seen = set()

        while n not in seen:
            seen.add(n)
            
            digits = [int(d) * int(d) for d in str(n)]
            n = sum(digits)
            if n == 1:
                return True 
            




        return False




        