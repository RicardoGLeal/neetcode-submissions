class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pacQueue, atlQueue = deque(), deque()

        # BFS from a given ocean's border cells
        # Expands uphill (height >= current) because we're reversing the flow direction:
        # instead of water flowing down to the ocean, the ocean "climbs up" to find reachable cells
        def bfs(queue, visited):
            while queue:
                r, c = queue.popleft()
                for dr, dc in ((1,0), (-1,0), (0,1), (0,-1)):
                    newRow, newCol = r + dr, c + dc

                    if (newRow >= 0 and newCol >= 0 and             # within grid bounds
                        newRow < ROWS and newCol < COLS and
                        (newRow, newCol) not in visited and         # not already visited
                        heights[newRow][newCol] >= heights[r][c]):  # neighbor is higher — water from it flows down to us
                            visited.add((newRow, newCol))
                            queue.append((newRow, newCol))

        pacVisited, atlVisited = set(), set()

        # Seed Pacific: border cells already touch the ocean, so mark them visited immediately
        for c in range(COLS):
            pacQueue.append((0, c))       # top row
            pacVisited.add((0, c))

        for r in range(ROWS):
            pacQueue.append((r, 0))       # left column
            pacVisited.add((r, 0))

        # Seed Atlantic: same idea for bottom row + right column
        for c in range(COLS):
            atlQueue.append((ROWS-1, c))  # bottom row
            atlVisited.add((ROWS-1, c))

        for r in range(ROWS):
            atlQueue.append((r, COLS-1))  # right column
            atlVisited.add((r, COLS-1))

        # Run BFS from both oceans to find all reachable cells
        bfs(pacQueue, pacVisited)
        bfs(atlQueue, atlVisited)

        # Any cell reachable by both oceans can drain to both — that's our answer
        result = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pacVisited and (r, c) in atlVisited:
                    result.append([r, c])
        return result