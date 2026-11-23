class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: list[list[int]], queries: list[list[int]]) -> list[bool]:
        # is_prereq[i][j] 代表課程 i 是否為課程 j 的先修課
        is_prereq = [[False] * numCourses for _ in range(numCourses)]
        
        for pre, course in prerequisites:
            is_prereq[pre][course] = True
            
        # Floyd-Warshall 計算傳遞閉包（注意：中繼點 k 必須放在最外層迴圈）
        for k in range(numCourses):
            for i in range(numCourses):
                if not is_prereq[i][k]:  # 小優化：若 i 到不了 k，直接跳過內層
                    continue
                for j in range(numCourses):
                    if is_prereq[k][j]:
                        is_prereq[i][j] = True
                        
        return [is_prereq[u][v] for u, v in queries]