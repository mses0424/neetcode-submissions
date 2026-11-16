# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        first = dummy
        for _ in range(left - 1):
            first = first.next
        curr = first.next
        for _ in range(right - left):
            nxt = curr.next
            curr.next = nxt.next
            nxt.next = first.next
            first.next = nxt

        return dummy.next
        

