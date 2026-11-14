class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        a = b = c = False
        for item in triplets:
            if item[0] <= target[0] and item[1] <= target[1] and item[2] <= target[2]:
                if item[0] == target[0]:
                    a = True
                if item[1] == target[1]:
                    b = True
                if item[2] == target[2]:
                    c = True
            if a and b and c:
                return True
        return a and b and c

