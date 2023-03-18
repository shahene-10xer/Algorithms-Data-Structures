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
        '''
        bfs
        '''
        if not root: return
        queue = collections.deque([root])
        
        while queue:
            prev = None
            for _ in range(len(queue)):
                current = queue.popleft()
                if prev:
                    prev.next = current
                prev = current
                
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)
        
        return root
                
        