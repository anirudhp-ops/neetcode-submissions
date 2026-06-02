# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head.next

        store = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        slow.next = None

        prev = None
        curr = second

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        while prev and store and store.next:
            dummy = store.next
            prev_dummy = prev.next

            store.next = prev
            prev.next = dummy

            store = store.next.next
            prev = prev_dummy

        if store is not None:
            store.next = prev