# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        # Linear Time
        
        """
        Iterative Solution:
        
            Since we are using a stack, we need to write it the other way around:
                    instead of Left -> Val -> Right
                    we write: Right -> Val -> Left
            
            Using isinstance() method to judge the type of the value 
                that just popped from the stack.
        """
        stack = [root]
        output = []
        while stack:
            tempNode= stack.pop()
            if tempNode:
                if isinstance(tempNode, TreeNode):
                    
                    stack.append(tempNode.right)
                    stack.append(tempNode.val)
                    stack.append(tempNode.left)
                else:
                    output.append(tempNode)
        return output
        
        
        """
        Recursive Solution:
        """
#         output = []
        
#         def helper(node):
#             if not node:
#                 return
            
#             helper(node.left)
#             output.append(node.val)
#             helper(node.right)
            
        
#         helper(root)
#         return output