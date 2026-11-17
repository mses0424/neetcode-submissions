# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        dummy = ListNode()
        curr = dummy
        for i, item in enumerate(lists):
            if item:
                node = item
                heapq.heappush(heap,(node.val,i,node))
        while heap:
            val, i, top = heapq.heappop(heap)
            curr.next = ListNode(val)
            if top.next:
                heapq.heappush(heap,(top.next.val,i,top.next))
            curr = curr.next
        return dummy.next
