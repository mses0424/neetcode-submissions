from collections import deque

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        # 使用 deque 作為佇列，操作時間複雜度為 O(1)
        radiant = deque()
        dire = deque()
        n = len(senate)
        
        # 1. 初始化，將 R 和 D 的初始索引位置分別放入佇列
        for i, char in enumerate(senate):
            if char == 'R':
                radiant.append(i)
            else:
                dire.append(i)
                
        # 2. 開始模擬回合制投票
        while radiant and dire:
            r_idx = radiant.popleft()
            d_idx = dire.popleft()
            
            # 索引小的先發制人，贏家進入下一回合 (索引 + n)
            if r_idx < d_idx:
                radiant.append(r_idx + n)
            else:
                dire.append(d_idx + n)
                
        # 3. 判斷誰的佇列還有剩餘
        return "Radiant" if radiant else "Dire"