class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not len(edges) == n - 1:
            
            return False
        graph = defaultdict(list)

        for k,v in edges:
            graph[k].append(v)
            graph[v].append(k)

        visited = set()

        def dfs(node, parent):
            if node in visited:
                return False

            visited.add(node)
            for child in graph[node]:
                if child == parent:
                    continue

                if not dfs(child, node):
                    return False
            
            return True
                
        return dfs(0, -1) and len(visited) == n
        