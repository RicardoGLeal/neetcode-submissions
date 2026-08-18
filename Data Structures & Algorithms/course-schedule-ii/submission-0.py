class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        graph = defaultdict(list)
        cleared = []

        for i,j in prerequisites:
            graph[i].append(j)

        visiting = set()

        def dfs(course):
            if course in visiting:
                return False

            if graph[course] == []:
                if course not in cleared:
                    cleared.append(course)
                return True

            visiting.add(course)
            for req in graph[course]:
                if not dfs(req):
                    return False
            visiting.remove(course)
            graph[course] = []
            cleared.append(course)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return []
        return cleared if len(cleared) > 0 else []