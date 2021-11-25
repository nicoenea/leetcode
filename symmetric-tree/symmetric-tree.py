# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        """ 
        Iterative 
        
        Use stack to traverse tree. If all has been traversed and there are non-symmetrical values, we return false
        
        if the program was not cut off until end, we return true
        """
        if not root:
            return True
        
        stack = [(root.left, root.right)]
        
        while stack:
            left, right = stack.pop()
            
            if not left and not right:
                continue
            if not left or not right or left.val != right.val:
                return False
            stack.append((left.left, right.right))
            stack.append((left.right, right.left))
        return True
        
        """
        Recursive:
        
        Use helper dfs function to complete problem
        if left and right, then will check if all values are symmetrical until reach leaf
        """
#         if not root:
#             return True
#         ans = None
        
#         def dfs(left, right):
#             if left and right:
#                 return left.val == right.val and dfs(left.left, right.right) and dfs(left.right, right.left)
#             return left == right
        
#         return dfs(root.left, root.right)