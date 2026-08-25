"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]'):

        if not head:
            return None

        curr = head 

        NewHead = Node(head.val)
        NewHead_curr = NewHead

        d = {}

        d[curr] = NewHead_curr

        while curr.next: 
            curr = curr.next 
            NewHead_curr.next = Node(curr.val)

            NewHead_curr = NewHead_curr.next
            d[curr] = NewHead_curr

        NewHead_curr = NewHead
        curr = head 
        
        while NewHead_curr: 
            if curr.random:
                NewHead_curr.random = d[curr.random]
            
            NewHead_curr = NewHead_curr.next 
            curr = curr.next 
        
        return NewHead
        
    


        
        