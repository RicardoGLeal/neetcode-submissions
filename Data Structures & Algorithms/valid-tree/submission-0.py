from collections import defaultdict

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) >= n:
            return False

        graphMap = defaultdict(list)

        for i,j in edges:
            graphMap[i].append(j)
            graphMap[j].append(i)
        
        visited = set()

        def dfs(node, parent):
            visited.add(node)

            for neighbor in graphMap[node]:
                if neighbor == parent:
                    continue
                if neighbor in visited:
                    return False
                if not dfs(neighbor, node):
                    return False
            return True
        
        return dfs(0, -1) and len(visited) == n