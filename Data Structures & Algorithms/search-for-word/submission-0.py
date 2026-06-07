class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # Approach: DFS + Backtracking
        # For every cell on the board, attempt to build the word starting from that cell.
        # At each step, we check if the current cell matches the expected letter in the word.
        # If it does, we mark it as visited and recursively explore all 4 neighbors for the next letter.
        # If a path fails, we backtrack by unmarking the cell so other paths can reuse it.
        # We succeed when the index reaches len(word), meaning all letters were matched in order.
        visited = set()

        def dfs(cords, index):
            # All letters matched — word found!
            if index == len(word):
                return True

            # Current cell is out of bounds
            if cords[0] >= len(board) or cords[1] >= len(board[0]) or cords[0] < 0 or cords[1] < 0:
                return False

            # Current cell already used in this path, or letter doesn't match
            if cords in visited or board[cords[0]][cords[1]] != word[index]:
                return False
            
            # Mark cell as visited for this path
            visited.add(cords)

            row = cords[0]
            col = cords[1]

            # Explore all 4 neighbors looking for the next letter
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            for dr, dc in directions:
                if dfs((row + dr, col + dc), index + 1):
                    return True

            # No direction worked — backtrack by unmarking this cell
            visited.remove(cords)
            return False

        # Try starting DFS from every cell on the board
        for r in range(len(board)):
            for c in range(len(board[0])):
                if dfs((r, c), 0):
                    return True
        
        return False