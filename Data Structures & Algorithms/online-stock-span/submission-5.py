class StockSpanner:

    def __init__(self):
        self.total = []
    def next(self, price: int) -> int:
        count = 1 
        if len(self.total) == 0:
            self.total.append((price,1))
            return 1
        while self.total[-1][0] <= price:
            count += self.total[-1][1]
            self.total.pop()
            if len(self.total) == 0:
                break
        self.total.append((price,count))
        return count


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)