# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if not root: return 0

        node_queue = deque([(root, root.val)])
        total_sum = 0
        while node_queue:
            cur_node, cur_sum = node_queue.popleft()
            if cur_node.left:
                node_queue.append((cur_node.left, cur_sum * 10 + cur_node.left.val))

            if cur_node.right:
                node_queue.append((cur_node.right, cur_sum * 10 + cur_node.right.val))

            if not cur_node.left and not cur_node.right:
                total_sum += cur_sum

        return total_sum