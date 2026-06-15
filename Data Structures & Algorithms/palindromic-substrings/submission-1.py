class Solution:
    def countSubstrings(self, s: str) -> int:
        # Approach: Expand Around Center
        # Every palindromic substring has a unique center — either a single
        # character (odd-length) or a gap between two characters (even-length).
        # For each possible center, we expand outward as long as the characters
        # on both sides match, counting one palindrome per successful expansion.
        # Time: O(n²) — n centers, each expanding up to O(n) steps
        # Space: O(1) — only a counter, no extra data structures

        nPal = 0  # total count of palindromic substrings found

        def expand(left, right):
            nonlocal nPal
            # Expand outward from the starting center (left, right).
            # Each successful match-and-move confirms one more palindrome,
            # so we increment the counter inside the loop body.
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
                nPal += 1
            return

        for i in range(len(s)):
            expand(i, i)      # odd-length:  center is character i        (e.g. "aba")
            expand(i, i + 1)  # even-length: center is gap between i, i+1 (e.g. "abba")

        return nPal