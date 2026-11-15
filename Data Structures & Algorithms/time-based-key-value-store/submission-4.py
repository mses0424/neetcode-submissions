class TimeMap:

    def __init__(self):
        self.total = defaultdict(list)
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.total[key].append((value,timestamp))    
    def get(self, key: str, timestamp: int) -> str:
        curr = self.total[key]
        if not curr or curr[0][1] > timestamp:
            return "" 
        start = 0 
        end = len(curr) 
        while start < end:
            mid = (start + end) // 2
            if curr[mid][1] < timestamp:
                start = mid + 1
            else:
                end = mid
        if start == len(curr) or curr[start][1] != timestamp:
            return curr[start-1][0] 
        else:
            return curr[start][0]
