from collections import deque

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: list[list[int]], queries: list[list[int]]) -> list[bool]:
        adj = [[] for _ in range(numCourses)]
        in_degree = [0] * numCourses
        # prereq_set[v] 記錄課程 v 的所有直接與間接先修課
        prereq_set = [set() for _ in range(numCourses)]
        
        for pre, course in prerequisites:
            adj[pre].append(course)
            in_degree[course] += 1
            
        queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
        
        while queue:
            curr = queue.popleft()
            for nxt in adj[curr]:
                # curr 本身與 curr 的所有先修課，都是 nxt 的先修課
                prereq_set[nxt].add(curr)
                prereq_set[nxt].update(prereq_set[curr])
                
                in_degree[nxt] -= 1
                if in_degree[nxt] == 0:
                    queue.append(nxt)
                    
        return [u in prereq_set[v] for u, v in queries]