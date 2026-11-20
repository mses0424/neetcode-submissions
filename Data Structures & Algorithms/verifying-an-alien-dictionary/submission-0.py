class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        total = {key:idx for idx, key in enumerate(order)}
        for i in range(len(words)-1):
            first, second = words[i], words[i+1]
            for j in range(min(len(first),len(second))):
                if first[j] != second[j]:
                    if total[first[j]] > total[second[j]]:
                        return False
                    break
            else:
                if len(first) > len(second):
                    return False
        return True
