class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # 第一階段：快慢指標在環內相遇（對應 LC 141）
        slow = nums[0]
        fast = nums[nums[0]]
        while slow != fast:
            slow = nums[slow]        # 慢指標走 1 步（相當於 slow = slow.next）
            fast = nums[nums[fast]]  # 快指標走 2 步（相當於 fast = fast.next.next）

        # 第二階段：尋找環的入口（對應 LC 142）
        # 讓一個指標退回起點 0，兩者改為每次各走 1 步，再次相遇處即為環的入口
        slow = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow