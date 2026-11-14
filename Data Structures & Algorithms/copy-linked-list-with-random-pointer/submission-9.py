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
        copyToList = {None: None}
        curr = head
        while curr:
            copy = Node(curr.val)
            copyToList[curr] = copy
            curr = curr.next
        curr = head

        while curr:
            copy = copyToList[curr]
            copy.next = copyToList[curr.next]
            copy.random = copyToList[curr.random]
            curr = curr.next
        return copyToList[head]

        
