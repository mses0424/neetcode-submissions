# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_sum = float('-inf')

        def dfs(node: Optional[TreeNode]) -> int:
            nonlocal max_sum
            if not node:
                return 0

            # 1. 計算左右子樹能帶來的最大單邊貢獻（若是負數直接取 0 捨棄）
            left_gain = max(0, dfs(node.left))
            right_gain = max(0, dfs(node.right))

            # 2. 以當前節點為轉折點的最高路徑和（包含左右兩邊）
            current_path_sum = node.val + left_gain + right_gain

            # 3. 更新全域最大值
            max_sum = max(max_sum, current_path_sum)

            # 4. 回傳給上一層父節點：只能選「單邊較大者」加上自己
            return node.val + max(left_gain, right_gain)

        dfs(root)
        return max_sum