class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxStr = 0
        newStr = deque()

        for i in s:
            while i in newStr and len(newStr) > 0:
                newStr.popleft()
            newStr.append(i)
            maxStr = max(maxStr, len(newStr))
            
        return maxStr 




