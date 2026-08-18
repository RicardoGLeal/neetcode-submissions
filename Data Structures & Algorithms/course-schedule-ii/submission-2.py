class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        graph = defaultdict(list)
        cleared = []

        for i,j in prerequisites:
            graph[i].append(j)

        order = []
        done = set()
        visiting = set()

        def dfs(course):
            if course in visiting:
                return False
            if course in done:
                return True

            visiting.add(course)
            for req in graph[course]:
                if not dfs(req):
                    return False
            visiting.remove(course)
            done.add(course)
            order.append(course)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return []
        return order