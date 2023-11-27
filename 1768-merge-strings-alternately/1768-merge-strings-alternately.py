class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        left=right=0
        n = len(word1)
        m = len(word2)
        result = ""
        while left < n and right < m:
            result += f"{word1[left]}{word2[right]}"
            left += 1
            right += 1
            
        while left < n:
            result += word1[left]
            left += 1
        while right < m:
            result += word2[right]
            right += 1
        return result