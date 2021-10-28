"""
    Singly LinkedList Implementation
"""

class ListNode:
    """
    Init ListNode Object
    """
    def __init__(self, val):
        self.val = val 
        self.next = None
        
class MyLinkedList(object):
    """
    Init your data structure 
    """
    #Takes nothing at first, to initialize Head(Sentinel) Node
    def __init__(self):
        # Starts at 0
        self.size = 0
        # Head of a linkedlist is always 0 or NULL
        # self.head = None 
        self.head = ListNode(0)
    """
    Find the predecessor of the node to insert. 
        If a node is to be inserted at head, its predecessor is a sentinel head.
        If a node is to be inserted at tail, its predecessor is the last node.
    """
    def addAtHead(self, val:int) -> None: # O(1) time and space complexity
        """
        Add a node of value 'val' before the first element of the LinkedList.
            After the insertion, the node will become the first node of the LinkedList
        ================
        O(1) time and space complexity | You are iterating the same regardless of the size of LinkedList
        """
        # use index 0 to get the head node in order to use as predecessor
        self.addAtIndex(0,val)
        
    def addAtTail(self, val:int) -> None:
        """
        Append a node of value 'val' to the last element of the LinkedList.
        ================
        O(N) time and O(1) space complexity
        """
        # use size of LinkedList in order to get last node and use as predecessor
        self.addAtIndex(self.size, val)
        
    def addAtIndex(self, index:int, val:int) -> None:
        """
        Add a node of value 'val' beofre the index-th node in the LinkedList.
            If index equals the length of the LinkedList, the node will be appended to the end of the LinkedList
            If index is greater than the length 'self.size', the node will not be inserted.
        ================
        O(index) time and  O(1) space complexity
        """
        if index > self.size:
            return 
        # needs to iterate size to add new node
        self.size += 1
        
        pred = self.head # First predecessor is head (singly linked list)
        
        #iterate through LinkedList through index-th amount of times
        for _ in range(index):
            pred = pred.next
        # Node to be added to list 
        to_add = ListNode(val)
        # Pointing to original predecessor
        to_add.next = pred.next
        # Add new node to next index
        pred.next = to_add
        
    def deleteAtIndex(self, index:int) -> None:
        """
        Delete the index-th node in the LinkedList.
            If index is not valid, will return -1
        ================
        O(index) time and  O(1) space complexity
        """
        #check to see if getting valid index
        if index < 0 or index >= self.size:
            return 
        
        #reduce the size, due to removing list node 
        self.size -= 1 
        
        pred = self.head
        #iterate through LinkedList through index-th amount of times
        for _ in range(index):
            pred = pred.next
        # Skip a connection because we are getting rid of the node 
        pred.next = pred.next.next
        
    def get(self, index:int) -> int:
        """
        Get the value of the index-th node in the LinkedList. 
            If the index is invalid, return -1
        ================
        O(index) time and  O(1) space complexity
        """
        #check to see if getting valid index
        if index < 0 or index >= self.size:
            return -1
            
        #start at head
        current = self.head
        
        #iterate through LinkedList through index-th amount of times
        for _ in range(index + 1):
            current = current.next
            
        return current.val 
        