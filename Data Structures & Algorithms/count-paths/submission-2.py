class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Approach: top-down DP (recursion + memoization).
        # State: dfs(r, c) = number of unique paths from (r, c) to the
        #   bottom-right corner, moving only down or right.
        # Recurrence: paths from a cell = paths from the cell below
        #   + paths from the cell to the right.
        # Base cases: off the grid -> 0 paths; at the goal -> 1 path.
        # Each (r, c) is reached by many paths, so we cache its result
        #   in dp to avoid recomputing the same subtree.
        # Time: O(m*n) — each cell computed once.  Space: O(m*n) for dp.

        dp = [[-1] * n for _ in range(m)]   # -1 = "not computed yet"

        def dfs(r, c):
            if r >= m or c >= n:            # walked off the grid
                return 0
            if r == m - 1 and c == n - 1:   # reached the goal: one path ends here
                return 1
            if dp[r][c] != -1:              # already solved this subproblem
                return dp[r][c]

            # sum the two ways out of this cell, then cache it
            res = dfs(r + 1, c) + dfs(r, c + 1)
            dp[r][c] = res
            return res

        return dfs(0, 0)