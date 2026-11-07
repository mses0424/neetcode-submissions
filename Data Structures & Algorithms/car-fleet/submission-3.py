class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        total = sorted(zip(position,speed),reverse=True)
        fleet = 0
        current = 0
        for i in range(len(total)):
            time = (target - total[i][0]) / total[i][1]
            if time > current:
                fleet += 1
                current = time
        return fleet