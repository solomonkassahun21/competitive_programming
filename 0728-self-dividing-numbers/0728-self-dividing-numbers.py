class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        result =[]
        
        for i in range(left,right+1):
            temp = i 
            while temp > 0:
                r = temp % 10
                
                if r ==0 or i % r != 0:
                    break
                temp = temp // 10
            if temp ==0:
                result.append(i)
        return result
                    
        