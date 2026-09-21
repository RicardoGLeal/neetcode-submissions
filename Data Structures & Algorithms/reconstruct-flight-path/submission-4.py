class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort()
        flightMap = {}
        for orig, dest in tickets:
            if orig not in flightMap:
                flightMap[orig] = []
            flightMap[orig].append(dest)
 
        for src in flightMap:
            flightMap[src].reverse()  # smallest destination ends up last, so pop() is O(1)
 
        res = []
 
        def dfs(src):
            while flightMap.get(src):
                nxt = flightMap[src].pop()
                dfs(nxt)
            res.append(src)  # postorder: only add src once every edge out of it is used
 
        dfs("JFK")
        return res[::-1]