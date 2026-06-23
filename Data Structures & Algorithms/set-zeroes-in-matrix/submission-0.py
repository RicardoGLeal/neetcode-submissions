class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        zero_rows, zero_cols = set(), set()

        for r in range(len(matrix)):
            for c in range(len(matrix[r])):
                if matrix[r][c] == 0:
                    zero_rows.add(r)
                    zero_cols.add(c)

        for r in range(len(matrix)):
            for c in range(len(matrix[r])):
                if r in zero_rows:
                    matrix[r][c] = 0
                elif c in zero_cols:
                    matrix[r][c] = 0