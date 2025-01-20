"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        

        d=deque()
        d.append(root)

        while d:
            d.append(None)
            for i in range(len(d)-1):
                k=d.popleft()
                if k:
                    k.next=d[0]
                    d.append(k.left)
                    d.append(k.right)
            d.popleft()
        return root
        