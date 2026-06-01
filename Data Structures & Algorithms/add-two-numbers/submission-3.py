# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0; 
        save = l1
        
        dummy = ListNode(0); 
        curr = dummy
        
        while (l1 and l2): 
            val = (l1.val + l2.val + carry) % 10 
            carry = (l1.val + l2.val + carry) // 10 
            newer = ListNode(val)
           
            dummy.next = newer; 
            dummy = dummy.next
            
            l1 = l1.next
            l2 = l2.next


        while l1 or l2 or carry: 
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            val = (v1 + v2 + carry) % 10 
            carry = (v1 + v2 + carry) // 10 
            newer = ListNode(val)

            dummy.next = newer; 
            dummy = dummy.next

            if l1: l1 = l1.next
            if l2: l2 = l2.next
        
        return curr.next
            
        
    



        