class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)

        for course, req in prerequisites:
            graph[course].append(req)

        visiting = set()

        def dfs(course):
            if course in visiting:
                return False

            if graph[course] == []:
                return True
            
            visiting.add(course)

            for req in graph[course]:
                if not dfs(req):
                    return False
            
            graph[course] = []
            visiting.remove(course)
            return True

        
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True