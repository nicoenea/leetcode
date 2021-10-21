# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def traverse(l1, l2, carry):
            if not l1 and not l2 and not carry:
                return None
            tmp = 0
            if l1:
                tmp+=l1.val
                l1 = l1.next
            if l2:
                tmp+=l2.val
                l2 = l2.next
            if carry:
                tmp+=1
                carry = False
            if tmp>=10: carry = True
            return ListNode(val = tmp%10, next=traverse(l1, l2, carry))
            
        return traverse(l1, l2, False)