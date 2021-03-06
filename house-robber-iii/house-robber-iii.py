# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        
        def helper(node):
            if not node:
                return (0, 0)
            
            left  = helper(node.left)
            right = helper(node.right)
            
            # if we rob this node, we cannot rob its children
            rob = node.val + left[1] + right[1]
            
            # choose to either rob its children or not
            not_rob = max(left) + max(right)
            
            return [rob, not_rob]
        
        return max(helper(root))
        