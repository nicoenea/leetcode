# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        result = 0
        # Use stack and DFS to iterate through the elements of tree
        stack = [(root, False)]
        while stack:
            curr, is_left = stack.pop() #pop current element and save value to curr, and isLeft[True|False]
            # If the curr value is "none" discard and continue
            if not curr:
                continue
            
            # save to result if the value is a left leaf
            if not curr.left and not curr.right:
                #print("curr left: {} , curr right: {}".format(curr.left, curr.right))
                if is_left:
                    result += curr.val
            else:
                #Continue stacking the rest of the tree
                stack.append((curr.left, True))
                stack.append((curr.right, False))
        return result
        