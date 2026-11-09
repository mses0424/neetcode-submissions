# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return (0,0)
            left, left_skip = dfs(node.left)
            right, right_skip = dfs(node.right)
            curr = node.val + left_skip + right_skip
            curr_skip = max(left,left_skip) + max(right,right_skip)
            return (curr,curr_skip)
        return max(dfs(root))