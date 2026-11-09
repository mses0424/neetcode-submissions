# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        current = [root]
        if not root:
            return []
        while current:
            level = []
            next_level = []
            for item in current:
                level.append(item.val)
                if item.left:
                    next_level.append(item.left)
                if item.right:
                    next_level.append(item.right)
            ans.append(level)
            current = next_level
        return ans