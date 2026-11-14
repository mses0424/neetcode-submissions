class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        total = Counter(hand)
        curr = min(total.keys())
        length = len(hand)
        while True:
            for i in range(curr,curr+groupSize):
                if total[i] < 1:
                    return False
                total[i] -= 1
            length -= groupSize
            if length == 0:
                break
            curr = min(item for item in total.keys() if total[item] != 0)
        return True