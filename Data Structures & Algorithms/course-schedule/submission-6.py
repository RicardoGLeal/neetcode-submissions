class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courses = defaultdict(list)
        reqMap = [0] * numCourses

        for course, req in prerequisites:
            courses[req].append(course)
            reqMap[course] += 1

        q = deque(c for c in range(numCourses) if reqMap[c] == 0)

        while q:
            node = q.popleft() # course without requisites.
            nexts = courses[node] # fetch courses which have node as requisite.

            for nxt in nexts:
                reqMap[nxt] -= 1
                if reqMap[nxt] == 0:
                    q.append(nxt)
                    
        return True if sum(reqMap) == 0 else False
                
            

        
        