class StockSpanner:

    def __init__(self):
        self.total = []
    def next(self, price: int) -> int:
        self.l = len(self.total)
        if self.l == 0:
            self.total.append(price)
            return 1
        self.count = 1
        while price >= self.total[self.l-1]:
            self.count += 1
            self.l -= 1
            if self.l < 1:
                break
        self.total.append(price)
        return self.count


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)