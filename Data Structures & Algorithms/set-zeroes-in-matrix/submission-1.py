class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        first_col_zero = False
        rows, cols = len(matrix), len(matrix[0])
        
        # identify 0s in the matrix

        for r in range(rows):
            if matrix[r][0] == 0: 
                first_col_zero = True

            for c in range(1, cols):
                if matrix[r][c] == 0:
                    matrix[r][0] = 0
                    matrix[0][c] = 0

            
        # apply flags to the interior
        for r in range(1, rows):
            for c in range(1, cols):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0

        # extend
        if matrix[0][0] == 0:
            for c in range(cols):
                matrix[0][c] = 0
        
        if first_col_zero:
            for r in range(rows):
                matrix[r][0] = 0

            

        




