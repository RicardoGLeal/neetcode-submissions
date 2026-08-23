class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        res = 0

        def dfs(x,y):
            # early return, out of bounds
            if x >= len(grid) or x < 0 or y >= len(grid[0]) or y < 0:
                return False

            # early return, already visited
            if (x,y) in visited:
                return False

            visited.add((x,y))

            if grid[x][y] == "1":
                for nX, nY in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
                    dfs(nX, nY)
                return True

        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if dfs(x,y):
                    res += 1
        return res
        