class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        self.res = 0
        visited = set()

        def dfs(r, c):
            # return if out of bounds
            if r >= len(grid) or c >= len(grid[0]) or r < 0 or c < 0:
                return
            
            # return if visited
            if (r, c) in visited:
                return

            if grid[r][c] == "1":
                visited.add((r,c))

                dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

                for i, j in dirs:
                    dfs(r+i, c+j)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1" and (i,j) not in visited:
                    self.res += 1
                dfs(i,j)
        return self.res
        