# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        
        def helper(node):
            if not node: # root is empty, return  0
                return 0 
            if not node.left and not node.right: # if root is not empty, return 1
                return 1
            
            l, r = helper(node.left) + 1, helper(node.right) + 1 #  check right/left for further depth
            
            if l > r: #if left side has more depth, return L, else R
                return l
            else:
                return r
            
        return helper(root)