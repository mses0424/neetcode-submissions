"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        total = {None: None}
        curr = head
        while curr:
            total[curr] = Node(curr.val)
            curr = curr.next
        curr = head
        while curr:
            copy = total[curr]
            copy.next = total[curr.next]
            copy.random = total[curr.random]
            curr = curr.next
        return total[head]