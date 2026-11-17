class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for item in nums:
            curr = []
            for result in res:
                curr.append(result+[item])
            res.extend(curr)
        return res