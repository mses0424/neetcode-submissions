# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def countt(head,k):
            now = 0
            curr = head
            while now < k and curr.next:
                curr = curr.next
                now += 1
            if now == k:
                return True
            else:
                return False
        def reversee(head,k):
            curr = head.next
            for _ in range(k-1):
                nxt = curr.next
                curr.next = nxt.next
                nxt.next = head.next
                head.next = nxt
            return curr
        dummy = ListNode()
        dummy.next = head
        prev = dummy
        while countt(prev,k):
            prev = reversee(prev,k)
        return dummy.next
