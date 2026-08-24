class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        rMap = defaultdict(list)
        best = float("inf")
        nBuses = 0

        for i,route in enumerate(routes):
            for stop in route:
                rMap[stop].append(i)
        
        q = deque()
        q.append(source)

        visitedRoutes, visitedStops = set(), set()
        visitedStops.add(source)

        if source == target:
            return 0

        while q:
            levelSize = len(q) # how many stops are in this level

            for _ in range(levelSize):
                stop = q.popleft()
            
                if stop == target:
                    return nBuses

                routesIdxs = rMap[stop]

                for route in routesIdxs:
                    if route in visitedRoutes:
                        continue

                    visitedRoutes.add(route)
                    stops = routes[route]

                    for nextStop in stops:
                        if nextStop in visitedStops:
                            continue

                        visitedStops.add(nextStop)
                        q.append(nextStop)
            nBuses += 1
                
        return best if best != float("inf") else -1 

            
        