class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * n for _ in range(m)]

        for r in range(m-1, -1, -1):
            for c in range(n-1, -1, -1):
                if r == m-1 or c == n-1:        # last row or last column: one straight path
                    dp[r][c] = 1
                else:                            # interior: paths down + paths right
                    dp[r][c] = dp[r+1][c] + dp[r][c+1]
        return dp[0][0]