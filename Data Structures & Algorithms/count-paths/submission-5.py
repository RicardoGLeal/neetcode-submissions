class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row = [0] * n

        for r in range(m-1, -1, -1):
            for c in range(n-1, -1, -1):
                if r == m-1 or c == n-1:        # last row or last column: one straight path
                    row[c] = 1
                else:                            # interior: paths down + paths right
                    row[c] = row[c] + row[c+1]
        # print(dp)
        return row[0]