class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        pos = []
        ans = []
        for i in range(len(asteroids)):
            if asteroids[i] > 0:
                pos.append(asteroids[i])
            else:
                if len(pos) == 0:
                    ans.append(asteroids[i])
                else:
                    a = pos[-1]
                    while a < -asteroids[i]:
                        pos.pop()
                        if len(pos) == 0:
                            ans.append(asteroids[i])
                            break
                        a = pos[-1]
                    if a == -asteroids[i]:
                        pos.pop()
        for item in pos:
            ans.append(item)   
        return ans