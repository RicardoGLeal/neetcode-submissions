class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Approach: for each unvisited land cell, increment the island count
        # and DFS-flood the entire connected island, marking all its cells as
        # visited. This way, the outer loop only ever triggers the counter on
        # cells that haven't been consumed by a prior flood.

        res = 0
        visited = set()

        def dfs(r, c):
            # out of bounds
            if r >= len(grid) or c >= len(grid[0]) or r < 0 or c < 0:
                return
            # already visited or water — nothing to flood
            if (r, c) in visited or grid[r][c] == "0":
                return

            # mark as visited and flood all 4 neighbors
            visited.add((r, c))
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                dfs(r + dr, c + dc)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                # unvisited land cell — new island found, flood it entirely
                if grid[i][j] == "1" and (i, j) not in visited:
                    res += 1
                    dfs(i, j)

        return res