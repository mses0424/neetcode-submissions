class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        new = []
        for i in range(len(points)):
            leng = points[i][0] ** 2 +  points[i][1] ** 2
            new.append((leng,points[i]))
        new.sort()
        ans = []
        for i in range(k):
            ans.append(new[i][1])
        return ans