# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        answer = '' # create string to hold value
        while head: # traverse through linkedlist
            answer += str(head.val) # store value in string
            head = head.next # move on to next node
        return int(answer, 2) # base for binary values is 2, so we include that in our conversion to int 
        