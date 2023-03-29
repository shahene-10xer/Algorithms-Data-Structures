"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

'''
0 -> 1 => 3 -> 2

stack = [Node(2)]
0 -> 1 -> <- 3 stack = [2]
what we want to do is append Node(2) to the end of list
'''

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        cur = head
        stack = []
        while cur:
            if cur.child:
                if cur.next:
                    stack.append(cur.next)
                cur.next = cur.child
                cur.child = None
                cur.next.prev = cur
            
            if not cur.next:
                break
            
            cur = cur.next
        
        while stack:
            cur.next = stack.pop()
            cur.next.prev = cur
            
            while cur.next:
                cur = cur.next
        return head
            
            
            
            