class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[-1] * n for _ in range(m)]

        for x in range(m-1, -1, -1):
            for y in range(n-1, -1, -1):
                if x == m-1 or y == n -1:
                    dp[x][y] = 1
                else:
                    dp[x][y] = dp[x+1][y] + dp[x][y+1]
        return dp[0][0]
