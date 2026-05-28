class Solution:
    # Most optimal Solution
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxStr = 0
        seenMap = {}  # maps character → its most recent index

        left = 0  # left boundary of the current window
        for right in range(len(s)):
            # If we've seen this char AND it's inside the current window,
            # jump left pointer just past the previous occurrence.
            # The >= left guard prevents left from jumping backwards
            # e.g. "tmmzuxt": when right=6 (char='t'), seen['t']=0
            # but left=2, so 0 >= 2 is False → left stays at 2 ✅
            # without the guard, left would wrongly jump back to 1 ❌
            if s[right] in seenMap and seenMap[s[right]] >= left:
                left = seenMap[s[right]] + 1

            # Update the character's latest index (whether new or duplicate)
            seenMap[s[right]] = right

            # Window size is right - left + 1
            maxStr = max(maxStr, right - left + 1)

        return maxStr

    
    def lengthOfLongestSubstringSetSol(self, s: str) -> int:
        seen = set()  # tracks unique characters in the current window
        left = 0      # left boundary of the current window
        maxLen = 0

        for right in range(len(s)):
            # If duplicate found, shrink window from the left
            # until the duplicate is removed
            # e.g. "abca": when right=3 (char='a'), left moves right
            # removing 'a' at index 0, giving window "bca" ✅
            while s[right] in seen:
                seen.remove(s[left])  # remove leftmost character
                left += 1             # shrink window from the left

            # Current character is not a duplicate, safe to add
            seen.add(s[right])

            # Window size is right - left + 1
            maxLen = max(maxLen, right - left + 1)

        return maxLen