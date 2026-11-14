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
        if not head:
            return None
        copyToList = {}
        curr = head
        while curr:
            copyToList[curr] = Node(curr.val)
            curr = curr.next
        curr = head
        if curr in copyToList:
            dummy = Node(0, copyToList[curr], 0)
        else:
            dummy = Node(0, None, 0)
        while curr:
            newHead = copyToList[curr]

            if curr.next in copyToList:
                newHead.next = copyToList[curr.next]
            else:
                newHead.next = None
            
            if curr.random in copyToList:
                newHead.random = copyToList[curr.random]
            else:
                newHead.random = None
            
            newHead = newHead.next
            curr = curr.next
        return dummy.next

        
