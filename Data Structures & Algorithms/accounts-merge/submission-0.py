class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        graph = defaultdict(set)
        email_to_name = {}

        for account in accounts:
            name = account[0]
            first_email = account[1]
        
            for email in account[1:]:
                graph[first_email].add(email)
                graph[email].add(first_email) # undirected: both directions
                email_to_name[email] = name

        visited = set()
        result = []

        def dfs(email, visited, component):
            visited.add(email)
            component.append(email)

            for neighbor in graph[email]:
                if neighbor not in visited:
                    dfs(neighbor, visited, component)

        for email in graph:
            if email not in visited:
                component = []
                dfs(email, visited, component)
                result.append([email_to_name[email], *sorted(component)])
        return result 


