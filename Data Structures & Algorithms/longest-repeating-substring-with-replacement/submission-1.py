class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        charMap = {}  # Tracks frequency of each character in the current window
        maxFreq = 0   # Tracks the highest frequency of any single char in the window
        res = 0 
        
        for r in range(len(s)):
            # Expand window by adding the right character
            charMap[s[r]] = charMap.get(s[r], 0) + 1

            # Update maxFreq if the current char has a higher frequency
            maxFreq = max(maxFreq, charMap[s[r]])

            # Shrink window from the left if replacements needed exceed k
            # replacements needed = window_size - most_frequent_char_count
            while (r - l + 1) - maxFreq > k:
                charMap[s[l]] -= 1  # Remove leftmost char from window
                l += 1              # Shrink window from the left

            # Current window [l, r] is valid, update result
            res = max(res, r - l + 1)

        return res






        