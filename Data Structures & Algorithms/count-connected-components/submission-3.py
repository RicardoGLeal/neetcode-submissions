class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        """
        APPROACH: Count connected components via DFS.

        A connected component is a maximal set of nodes all reachable from
        one another. To count them: start a fresh DFS from every node we
        haven't visited yet. Each time we *start* a new DFS, we've found a
        node that no previous DFS could reach -- i.e. a brand-new component.
        So the number of DFS starts == the number of components.

        The DFS itself floods outward from its start node, marking every
        node in that component as visited. That's what guarantees later
        nodes in the same component won't trigger a second (false) start.

        Isolated nodes (no edges) are handled automatically: iterating over
        range(n) reaches them, their adjacency list is empty, so DFS just
        marks the single node and returns -- one start, one component.

        Time:  O(V + E) -- each node visited once, each edge traversed twice.
        Space: O(V + E) -- adjacency list, plus O(V) for visited and the
               recursion stack.

        Where V is the number of vertices and E is the number of edges in the graph.
    
        """
        # Build an undirected adjacency list: every edge goes both ways.
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        visited = set()

        def dfs(node):
            # Mark first, then recurse: this "register-before-recurse" order
            # prevents infinite loops on cycles (a neighbor that points back
            # to us finds us already visited).
            visited.add(node)
            for neighbor in graph[node]:   # graph[node] is [] for isolated nodes
                if neighbor not in visited:
                    dfs(neighbor)

        components = 0
        for node in range(n):          # range(n), not graph.keys(), so we
            if node not in visited:    # don't miss isolated nodes
                dfs(node)              # flood the whole component...
                components += 1        # ...and count it as one
        return components