class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        if s[-1] == '1':
            return False
        queue = deque([0])
        farthest = 0     
        while queue:
            i = queue.popleft()
            start = max(farthest + 1, i + minJump)
            end = min(len(s) - 1, i + maxJump)
            for j in range(start, end + 1):
                if s[j] == '0':
                    queue.append(j)
                    if j == len(s) - 1:
                        return True
            farthest = max(farthest, end)
        return False