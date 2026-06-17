class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Approach: bottom-up DP, space-optimized to a single row.
        # The full m*n table fills bottom-to-top, and each row only ever
        #   reads the row directly below it — so we keep just ONE array
        #   and overwrite it row by row, from the bottom row up to the top.
        # At any moment, before we overwrite row[c]:
        #   - row[c]   = the cell BELOW  (value from the previous row)
        #   - row[c+1] = the cell to the RIGHT (already updated this pass,
        #                since we walk columns right-to-left)
        # Base cases: last row and last column are all 1 (one straight path).
        # Time: O(m*n).  Space: O(n) — one row instead of the full grid.

        row = [0] * n

        for r in range(m - 1, -1, -1):              # rows: bottom to top
            for c in range(n - 1, -1, -1):          # cols: right to left
                if r == m - 1 or c == n - 1:        # edge: single straight path
                    row[c] = 1
                else:                                # interior: down + right
                    row[c] = row[c] + row[c + 1]
        return row[0]                                # paths from the top-left corner