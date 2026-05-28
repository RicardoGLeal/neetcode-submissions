class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxStr = 0
        seenMap = {}

        left = 0
        for right in range(len(s)):
            if s[right] in seenMap and seenMap[s[right]] >= left:
                left = seenMap[s[right]] + 1
            seenMap[s[right]] = right
            maxStr = max(maxStr, right - left + 1)
            
        return maxStr 




