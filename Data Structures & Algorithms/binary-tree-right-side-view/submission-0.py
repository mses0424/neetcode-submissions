# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        ans = []
        queue = deque([root])
        while queue:
            s = len(queue) - 1
            for _ in range(s):
                a = queue.popleft()
                if a.left:
                    queue.append(a.left)
                if a.right:
                    queue.append(a.right)
            b = queue.popleft()
            if b.left:
                queue.append(b.left)
            if b.right:
                queue.append(b.right)
            ans.append(b.val)
        return ans
            

