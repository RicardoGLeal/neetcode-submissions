class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Approach: Expand Around Center
        # Every palindrome has a center — either a single character (odd-length)
        # or a gap between two characters (even-length).
        # We iterate over every index, treating it as a potential center,
        # and expand outward as long as characters match on both sides.
        # We keep track of the longest palindrome found across all centers.
        # Time: O(n²) — n centers, each expanding up to O(n) steps
        # Space: O(1) — only tracking indices, no extra data structures

        bestL, bestR = 0, 0  # indices of the longest palindrome found so far

        def expand(left, right):
            # Expand outward from the starting center (left, right)
            # as long as characters match and we stay within bounds
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            # Loop exits one step too far in each direction, so correct by 1
            return left + 1, right - 1

        def updateBest(l, r):
            nonlocal bestL, bestR
            # Update the best palindrome if the current one is longer
            if r - l + 1 > bestR - bestL + 1:
                bestL, bestR = l, r

        for i in range(len(s)):
            updateBest(*expand(i, i))      # odd-length: single character center
            updateBest(*expand(i, i + 1))  # even-length: gap between i and i+1

        return s[bestL:bestR + 1]  # slice the longest palindrome found