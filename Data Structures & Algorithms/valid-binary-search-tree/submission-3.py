# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        total = []
        curr = root
        ans = []
        while curr or total:
            while curr:
                total.append(curr)
                curr = curr.left
            curr = total.pop()
            ans.append(curr.val)
            curr = curr.right
        for i in range(len(ans)-1):
            if ans[i+1] - ans[i] <= 0:
                return False
        return True
