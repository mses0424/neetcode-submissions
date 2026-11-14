class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        count = Counter(hand)
        for card in sorted(count.keys()):
            if count[card] > 0:
                start_count = count[card]
                for i in range(card, card + groupSize):
                    if count[i] < start_count:
                        return False 
                    count[i] -= start_count
        return True