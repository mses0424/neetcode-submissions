class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five = 0
        ten = 0
        if len(bills) == 0:
            return True
        if bills[0] != 5:
            return False
        for item in bills:
            if item == 5:
                five += 1
            if item == 10:
                ten += 1
                if five < 1:
                    return False
                five -= 1
            if item == 20:
                if ten < 1:
                    if five < 3:
                        return False
                    else:
                        five -= 3
                else:
                    ten -= 1
                    if five < 1:
                        return False
                    else:
                        five -= 1
        return True