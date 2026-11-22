class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        visit = set(deadends)
        if "0000" in visit:
            return -1
        def get_neighbors(code: str):
            res = []
            for i in range(4):
                digit = int(code[i])
                for move in (-1, 1):
                    new_digit = (digit + move) % 10
                    res.append(code[:i] + str(new_digit) + code[i+1:])
            return res
        queue = deque([("0000", 0)])
        visit.add("0000")
        while queue:
            code, turns = queue.popleft()
            if code == target:
                return turns
            for nxt in get_neighbors(code):
                if nxt not in visit:
                    visit.add(nxt)
                    queue.append((nxt, turns + 1))

        return -1