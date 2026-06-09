class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        coursesMap = {}
        validCourses = set()

        # 1. Create representation of graph as a hashSet 
        for course, prerequisite in prerequisites:
            if course not in coursesMap:
                coursesMap[course] = set()
            coursesMap[course].add(prerequisite)

        def dfs(course, reqs, visited):
            # Return when cycle detected
            if course in visited:
                return False

            visited.add(course)

            # DFS all the req courses
            for req in reqs:
                if req in coursesMap and req not in validCourses:
                    if dfs(req, coursesMap[req], visited) == False:
                        return False
            validCourses.add(course)
            return True

        for course, reqs in coursesMap.items():
            if dfs(course, reqs, set()) == False:
                return False
        return True 
            



