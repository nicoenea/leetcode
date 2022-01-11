# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        
        self.total = 0 
        
        def helper(root, nums):
            # nums = ""
            
            #once we have finished traversing the tree, calculate the sum of numbers
            if not root.left and not root.right:
                nums += str(root.val)
                self.total += int(nums, 2)
                return
            
            # DFS Preorder traversal
            nums += str(root.val)
            if root.left:
                helper(root.left, nums)
            if root.right:
                helper(root.right, nums)
                
        # Start recursion
        helper(root, "")
        
        # return sum of numbers
        return self.total
            