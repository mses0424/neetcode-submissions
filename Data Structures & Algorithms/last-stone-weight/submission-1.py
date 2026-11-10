class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            stones.sort()
            first = stones[-1]
            second = stones[-2]
            if first == second:
                stones.pop()
                stones.pop()
            elif first > second:
                diff = first - second
                stones.pop()
                stones.pop()
                stones.append(diff)
        return 0 if len(stones) == 0 else stones[0]