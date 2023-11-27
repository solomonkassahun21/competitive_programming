class Solution:
    def countPrimes(self, n: int) -> int:
        count = 0
        if  n < 2:
            return 0
        d = [True for _ in range(n)]
        d[0] = d[1] = False
        
        i = 2
        
        while i * i < n:
            if d[i]:
                j = 2 * i 
                
                while j < n:
                    d[j] = False
                    j += i
            i += 1
            
        for item in d:
            if  item:
                count += 1
        return count
                
        
            
        