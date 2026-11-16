# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        def reverse(head):
            curr = head
            prev = None
            while curr:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            return prev
        now = reverse(head)
        rev = now
        if n == 1:
            temp = now.next
            now = None
            return reverse(temp)
        while n > 2:
            n -= 1
            now = now.next
        temp1 = now.next
        temp2 = now.next.next
        now.next = temp2
        temp1 = None
        return reverse(rev)
