"""
Longest Common Subsequence  —  2D bottom-up DP

State:  dp[i][j] = length of the LCS of text1[:i] and text2[:j]
        (row 0 / col 0 = empty prefix, so they stay 0 = base case)

Recurrence (look at the last char of each prefix):
        match     dp[i][j] = 1 + dp[i-1][j-1]      # take the shared char + best of what's before it
        no match  dp[i][j] = max(dp[i-1][j],        # drop last char of text1
                                  dp[i][j-1])        # drop last char of text2

Loop order (row by row, left to right) guarantees the three cells a
cell depends on (up, left, diagonal) are already filled.

Answer: dp[-1][-1] = dp[m][n] = the full text1 vs full text2.

Time  O(m * n)   Space  O(m * n)
"""


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)

        # (m+1) x (n+1) grid, pre-filled with base-case zeros
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):          # +1 so the last row is included
            for j in range(1, n + 1):      # +1 so the last col is included
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]      # match -> diagonal + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])  # no match -> best neighbor

        return dp[-1][-1]                  # bottom-right = full problem
        
#     x "a  b  c"
# "a"
# "b"
# "c"
# "d"
# "e"