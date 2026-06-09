from collections import defaultdict
from typing import List

class Solution:
    """
    Approach: Directed graph cycle detection via DFS with three node states.

    We model the problem as a directed graph where each node is a course
    and each edge (a -> b) means "a requires b". The question becomes:
    does this graph contain a cycle? If yes, we can never complete all courses.

    Each node has one of three states:
      - Unvisited:     not yet explored
      - Visiting:      currently on the DFS path (cycle if seen again)
      - Done:          fully explored, confirmed cycle-free

    We DFS every node. If we encounter a node already in `visiting`,
    we've found a cycle. If it's already in `validCourses`, it's safe to skip.
    """

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Build adjacency list: course -> list of its prerequisites
        graph = defaultdict(list)
        
        for course, prereq in prerequisites:
            graph[course].append(prereq)

        visiting = set()      # nodes on the current DFS path
        validCourses = set()  # nodes confirmed to have no cycle

        def dfs(course) -> bool:
            # Cycle detected: course is already on our current path
            if course in visiting:
                return False

            # Already confirmed safe: no need to re-explore
            if course in validCourses:
                return True

            # Mark as currently being visited
            visiting.add(course)

            # Recursively visit all prerequisites
            for prereq in graph[course]:
                if not dfs(prereq):
                    return False

            # Done exploring: remove from path, mark as safe
            visiting.remove(course)
            validCourses.add(course)
            return True

        # Run DFS from every course (graph may be disconnected)
        for course in range(numCourses):
            if not dfs(course):
                return False

        return True