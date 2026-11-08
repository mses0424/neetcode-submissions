class FreqStack:

    def __init__(self):
        self.count = defaultdict(int)
        self.total = defaultdict(list)
        self.maxf = 0
    def push(self, val: int) -> None:
        self.count[val] += 1
        self.total[self.count[val]].append(val)
        self.maxf = max(self.maxf,self.count[val])
    def pop(self) -> int:
        a = self.total[self.maxf].pop()
        self.count[a] -= 1
        if len(self.total[self.maxf]) == 0:
            self.maxf -= 1
        return a         


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()