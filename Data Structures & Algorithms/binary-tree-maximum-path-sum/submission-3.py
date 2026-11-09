# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        b = float('-inf')
        def dfs(node):
            nonlocal b
            if not node:
                return 0
            node_left = dfs(node.left)
            node_right = dfs(node.right)
            a = max(node_left+node.val,node_right+node.val,node.val)
            print(a)
            b = max(b,a,node_left+node.val+node_right)
            return a
        dfs(root)
        return b