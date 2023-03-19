# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # step1 - reverse both lists 
        l1_reversed = self.reverse_list(l1)
        l2_reversed = self.reverse_list(l2)
        
        # add numbers and create new linked list (Add Numbers I)
        carry = 0
        dummy = ListNode(0)
        cur = dummy
        while l1_reversed or l2_reversed or carry:
            l1_val = l1_reversed.val if l1_reversed else 0
            l2_val = l2_reversed.val if l2_reversed else 0
            val = l1_val + l2_val + carry
            carry = val // 10
            val = val % 10
            
            cur.next = ListNode(val)
            cur = cur.next
            l1_reversed = l1_reversed.next if l1_reversed else None
            l2_reversed = l2_reversed.next if l2_reversed else None 
        
        return self.reverse_list(dummy.next)
        
        
        
    
    def reverse_list(self, head):
        prev = None
        cur = head
        while cur:
            tmp = cur.next
            cur.next = prev
            prev, cur = cur, tmp
        
        return prev
            