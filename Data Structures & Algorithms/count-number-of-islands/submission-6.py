class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0

        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == "1":
                    res += 1
                    grid[x][y] = "0"

                    q = deque()
                    q.append((x,y))

                    while q:
                        r,c = q.popleft()
                        for nR, nC in [(r+1, c), (r-1, c), (r, c+1), (r,c-1)]:
                            if nR < 0 or nR >= len(grid) or nC < 0 or nC >= len(grid[0]):
                                continue

                            if grid[nR][nC] == "1":
                                grid[nR][nC] = "0"
                                q.append((nR, nC))
        return res






        