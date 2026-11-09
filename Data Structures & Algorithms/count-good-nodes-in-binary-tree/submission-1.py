# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        total = []
        total.append((root,root.val))
        ans = 1
        while total:
            a = total.pop()
            if a[0].left:
                if a[0].left.val >= a[1]:
                    ans += 1
                    total.append((a[0].left,a[0].left.val))
                else:
                    total.append((a[0].left,a[1]))
            if a[0].right:
                if a[0].right.val >= a[1]:
                    ans += 1
                    total.append((a[0].right,a[0].right.val))
                else:
                    total.append((a[0].right,a[1]))
        return ans
            

