class Solution:
    def longestPalindrome(self, s: str) -> str:
        left, right = 0, 0

        def expand(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            # when the loop exits, we've gone one step too far
            return left + 1, right - 1
                
        for i in range(len(s)):
            l, r = expand(i, i)
            lEven, rEven = expand(i, i+1)
            if r-l + 1 > right-left + 1:
                left = l
                right = r
            if rEven-lEven + 1 > right-left + 1:
                left = lEven
                right = rEven
        return s[left:right+1]



            