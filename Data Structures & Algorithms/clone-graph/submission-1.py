class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        visited = {}  # maps original node → its clone

        def dfs(node):
            if not node:
                return None
            
            # if already cloned, return the existing clone to avoid infinite loop on cycles
            if node in visited:
                return visited[node]

            # create clone and register it BEFORE recursing into neighbors
            # so that any cycle back to this node finds it in visited
            newNode = Node(node.val)
            visited[node] = newNode

            # recursively clone each neighbor and wire it to the new node
            for neighbor in node.neighbors:
                newNode.neighbors.append(dfs(neighbor))
            
            return newNode

        return dfs(node)