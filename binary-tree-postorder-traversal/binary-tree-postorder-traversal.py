# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        Iterative Solution
        
        
        Since we are using a stack, we need to write it the other way around:
                    instead of Val -> Right -> Left
                    we write: Left -> Right -> Val
            
            Using isinstance() method to judge the type of the value 
                that just popped from the stack.
        """
        stack = [root]
        output = []
        while stack:
            tempNode= stack.pop()
            if tempNode:
                if isinstance(tempNode, TreeNode):
                    stack.append(tempNode.val)
                    stack.append(tempNode.right)
                    stack.append(tempNode.left)
                else:
                    output.append(tempNode)
        return output
        
        
        
        """
        Recursive solution
        """
#         output = []
        
#         def helper(node):
#             if not node:
#                 return
        
#             helper(node.left)
#             helper(node.right)
#             output.append(node.val)
            
#         helper(root)
#         return output