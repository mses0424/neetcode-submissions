class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy
        up = 0

        # 只要 l1 還沒走完、l2 還沒走完、或還有進位 up，就繼續往下算
        while l1 or l2 or up:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            up, val = divmod(v1 + v2 + up, 10)  # 同時算出商數（新進位）與餘數（當前位數）
            curr.next = ListNode(val)           # 確定有這一位數才建節點，不需事後砍尾巴
            curr = curr.next

            if l1: l1 = l1.next
            if l2: l2 = l2.next

        return dummy.next