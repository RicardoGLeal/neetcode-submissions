class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Rotate the n×n matrix 90° clockwise, in place.
        Strategy: transpose across the main diagonal, then reverse each row.
        """
        n = len(matrix)

        # Phase 1: transpose — swap matrix[r][c] with matrix[c][r].
        # c starts at r + 1 so each off-diagonal pair is swapped exactly
        # once; looping the full row would swap every pair twice and undo
        # the work. The diagonal (r == c) maps to itself, so it's skipped.
        for r in range(n):
            for c in range(r + 1, n):
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]

        # Phase 2: reverse each row left-to-right.
        # After the transpose, every row holds the right values but in
        # reverse order; flipping each row lands them in rotated position.
        # r.reverse() mutates the inner list in place (no rebinding), so
        # the in-place constraint holds.
        for r in matrix:
            r.reverse()