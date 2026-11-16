# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        up = 0
        curr = head
        while l1 and l2:
            now = l1.val + l2.val + up
            if now > 9:
                up = 1
                now = now % 10
            else:
                up = 0
            curr.val = now
            new = ListNode()
            prev = curr
            curr.next = new
            curr = new
            l1 = l1.next
            l2 = l2.next
        if not l1 and not l2:
            if up == 1:
                curr.val = 1
            else:
                prev.next = None
        while not l1 and l2:
            now = l2.val + up
            if now > 9:
                up = 1
                now = now % 10
            else:
                up = 0
            curr.val = now
            new = ListNode()
            prev = curr
            curr.next = new
            curr = new
            l2 = l2.next
        if not l1 and not l2:
            if up == 1:
                curr.val = 1
            else:
                prev.next = None
        while l1 and not l2:
            now = l1.val + up
            if now > 9:
                up = 1
                now = now % 10
            else:
                up = 0
            curr.val = now
            new = ListNode()
            prev = curr
            curr.next = new
            curr = new
            l1 = l1.next
        if not l1 and not l2:
            if up == 1:
                curr.val = 1
            else:
                prev.next = None
        return head