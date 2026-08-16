"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        graph = {}

        def dfs(node):
            if not node:
                return

            if node in graph:
                return graph[node]

            clone = Node(node.val, [])
            graph[node] = clone
            
            for nei in node.neighbors:
                clone.neighbors.append(dfs(nei))
            return clone

        return dfs(node)



        