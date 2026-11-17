class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        nums.sort()
        for num in nums:
            curr = []
            for item in res:
                curr.append(item + [num])
                if (item + [num]) in res:
                    curr.pop()
            res.extend(curr)
        return res
