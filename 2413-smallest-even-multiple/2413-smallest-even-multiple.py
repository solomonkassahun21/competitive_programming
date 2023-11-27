class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        output = n
        while (True):
            if (output % n == 0 and output %2 == 0):
                return output
            output +=1
        