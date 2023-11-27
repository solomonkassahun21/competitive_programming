class Solution:
    def isPalindrome(self, x: int) -> bool:
        result  = 0
        temp = x
        while temp > 0:
            result = result * 10 + temp % 10
            temp //= 10
        return result == x
        
        