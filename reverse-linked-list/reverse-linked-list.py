# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        """
        Use a single liner to easily remember this, as it may be part of a bigger problem.
        
        To break it down:
            While we have a head (head!= none):
                 #1. Reverse  (head.next = prev)
                #2. Update Current (move to next node)
                #3. Update previous (make current node become prev node)
        """
        prev = None
        while head:
            head.next, head, prev = prev, head.next, head
        return prev