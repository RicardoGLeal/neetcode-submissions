class Solution:
    def countSubstrings(self, s: str) -> int:
        nPal = 0
        def expand(left, right):
            nonlocal nPal
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
                nPal += 1
            return

        for i in range(len(s)):
            expand(i,i)
            expand(i, i+1)
        return nPal