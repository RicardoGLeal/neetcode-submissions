class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxStr = 0
        seenSet = set()

        left = 0
        for right in range(len(s)):
            while s[right] in seenSet and len(seenSet) > 0:
                seenSet.remove(s[left])
                left += 1
            seenSet.add(s[right])
            maxStr = max(maxStr, len(seenSet))
            
        return maxStr 




