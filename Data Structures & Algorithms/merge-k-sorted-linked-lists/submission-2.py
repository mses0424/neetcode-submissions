class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
            
        n = len(lists)
        interval = 1
        
        # 當間隔小於串列數量時，持續進行兩兩合併
        while interval < n:
            for i in range(0, n - interval, interval * 2):
                lists[i] = self.mergeTwoLists(lists[i], lists[i + interval])
            # 每輪合併完，間隔放大兩倍
            interval *= 2
            
        return lists[0]
        
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy
        
        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next
            
        # 把剩下的部分接上去
        curr.next = l1 if l1 else l2
        
        return dummy.next