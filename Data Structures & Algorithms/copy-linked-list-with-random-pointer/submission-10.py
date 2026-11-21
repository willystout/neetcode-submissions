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

        nodeMap = {None : None}

        cur = head
        while cur:
            nodeMap[cur] = Node(0)
            cur = cur.next

        cur = head
        newNode = nodeMap[head]
        while cur:
            newNode.val = cur.val
            newNode.random = nodeMap[cur.random]
            newNode.next = nodeMap[cur.next]
            cur = cur.next
            newNode = newNode.next

        dummy = Node(0, nodeMap[head])
        return dummy.next
        