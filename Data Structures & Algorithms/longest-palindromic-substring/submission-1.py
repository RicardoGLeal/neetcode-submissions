class Solution:
    def longestPalindrome(self, s: str) -> str:
        bestL, bestR = 0, 0

        def expand(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            # when the loop exits, we've gone one step too far
            return left + 1, right - 1

        def updateBest(l, r):
            nonlocal bestL, bestR
            if r-l + 1 > bestR-bestL + 1:
                bestL = l
                bestR = r

        for i in range(len(s)):
            updateBest(*expand(i, i))
            updateBest(*expand(i, i+1))
            
        return s[bestL:bestR+1]



            