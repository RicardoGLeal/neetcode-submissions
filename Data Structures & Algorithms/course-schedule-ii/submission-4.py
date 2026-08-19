class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        reqMap = [0] * numCourses
        res = []

        for c, req in prerequisites:
            graph[req].append(c)
            reqMap[c] += 1

        q = deque(c for c in range(numCourses) if reqMap[c] == 0)

        while q:
            node = q.popleft()
            res.append(node)
            for nxt in graph[node]:
                reqMap[nxt] -= 1
                if reqMap[nxt] == 0:
                    q.append(nxt)
        return res if len(res) == numCourses else []


        







        