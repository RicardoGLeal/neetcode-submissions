from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        """
        Spiral Matrix  (LeetCode 54)

        Strategy: four shrinking boundaries.
        We peel one full edge at a time and pull that boundary inward,
        so a cell is never visited twice -- no `visited` set needed.

        top / bottom : first and last LIVE row indices
        left / right : first and last LIVE column indices

        The loop runs while a live rectangle still exists:
        top <= bottom AND left <= right.

        Time : O(m * n)  -- each cell appended exactly once
        Space: O(1)      -- excluding the output list
        """
        res = []
        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1

        while top <= bottom and left <= right:
            # 1. top row, walk LEFT -> RIGHT, then retire this row
            for c in range(left, right + 1):
                res.append(matrix[top][c])
            top += 1

            # 2. right column, walk TOP -> BOTTOM, then retire this column
            for r in range(top, bottom + 1):
                res.append(matrix[r][right])
            right -= 1

            # 3. bottom row, walk RIGHT -> LEFT.
            #    Guard: after step 1 advanced `top`, a single remaining
            #    row would already be consumed; without this check a thin
            #    matrix re-walks it. Only proceed if a row is still live.
            if top <= bottom:
                for c in range(right, left - 1, -1):
                    res.append(matrix[bottom][c])
                bottom -= 1

            # 4. left column, walk BOTTOM -> TOP.
            #    Same guard for a single remaining column after step 2.
            if left <= right:
                for r in range(bottom, top - 1, -1):
                    res.append(matrix[r][left])
                left += 1

        return res