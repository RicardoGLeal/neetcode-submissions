class Solution:

    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graphMap = defaultdict(list)

        for item in edges:
            graphMap[item[0]].append(item[1])
            graphMap[item[1]].append(item[0])

        visited = set()

        def dfs(node, neighbors):
            if node in visited:
                return
            visited.add(node)
            
            for n in neighbors:
                dfs(n, graphMap[n])
            return

        res = 0
        for node, neighbors in graphMap.items():
            if node not in visited:
                dfs(node, neighbors)
                res += 1
        res += n-len(graphMap)
        return res

        


