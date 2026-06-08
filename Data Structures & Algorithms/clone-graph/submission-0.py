"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        visited = {}

        def dfs(node):
            if not node:
                return
            
            if node in visited:
                return visited[node]

            newNode = Node(node.val)
            visited[node] = newNode

            newNode.neighbors = []
            for neighbor in node.neighbors:
                newNode.neighbors.append(dfs(neighbor))
            return newNode
        
        if not node:
            return
            
        dfs(node)
        return visited[node]