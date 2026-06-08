class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        self.res = 0
        visited = []

        def dfs(r, c, prevIsland):
            # return if out of bounds
            if r >= len(grid) or c >= len(grid[0]) or r < 0 or c < 0:
                return
            
            # return if visited
            if (r, c) in visited:
                return

            visited.append((r,c))
            
            if grid[r][c] == "1":
                if not prevIsland:
                    self.res += 1
                    prevIsland = True
                dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

                for i, j in dirs:
                    dfs(r+i, c+j, prevIsland)

        for i in range(len(grid)):
            for j in range(len(grid[0])):

                dfs(i,j, False)
        return self.res
        