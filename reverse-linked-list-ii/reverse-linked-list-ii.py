# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right: return head
        # 1) Get to position left
        # 2) Save node before left, reverse from left to right
        # 3) Connect ptrs
        dummy = ListNode(0, head)
        leftPrev, cur = dummy, head
        
        for _ in range(left - 1):
            leftPrev = cur
            cur = cur.next
        prev = None
        for _ in range(right - left + 1):
            tmpNext = cur.next
            cur.next = prev
            prev, cur = cur, tmpNext
        
        leftPrev.next.next = cur
        leftPrev.next = prev
        
        return dummy.next 
            
    