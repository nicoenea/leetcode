# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        
        """
        Iterative Solution:
        
            Since we are using a stack, we need to write it the other way around:
                    instead of Val -> Left -> Right
                    we write: Right -> Left -> Val
            
            Using isinstance() method to judge the type of the value 
                that just popped from the stack.
        """
#         stack = [root]
#         output = []
        
#         while stack:
#             tempNode = stack.pop()
            
#             if tempNode:
#                 if isinstance(tempNode, TreeNode):
#                     stack.append(tempNode.left)
#                     stack.append(tempNode.right)
#                     stack.append(tempNode.val)
#                 else:
#                     output.append(tempNode)
#         return output
                
        
        """
        Recursive Solution:
        
            using a helper function
        """
        
        output = []
        
        def helper(node):
            if not node:
                return
            output.append(node.val)
            helper(node.left)
            helper(node.right)
            
        helper(root)
        return output