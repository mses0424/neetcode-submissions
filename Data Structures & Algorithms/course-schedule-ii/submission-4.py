class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        total = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses
        for item in prerequisites:
            total[item[1]].append(item[0])
            indegree[item[0]] += 1
        ans = []
        curr = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                curr.append(i)
        print(total)
        while curr:
            now = curr.popleft()
            ans.append(now)
            for i in total[now]:
                indegree[i] -= 1
                if indegree[i] == 0:
                    curr.append(i)
        if len(ans) != numCourses:
            return []
        return ans