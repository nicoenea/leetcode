# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
       
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Two pointer iterative solution:
        
            1. Assign slow and fast pointers to head
            2. fast will move twice on each pass
            3. slow will move once each pass
            4. fast will reach the end of the list first, and when it does, the slow pointer will be at the middle of the list
                    so we return slow
            
        """
        slow = fast = head # 1 
        
        while fast: 
            
            fast = fast.next # 2
            if fast: 
                fast = fast.next # 2
            else:
                break  # Will break when fast reaches the end of the list
            
            slow= slow.next # 3
            
        return slow # 4 
