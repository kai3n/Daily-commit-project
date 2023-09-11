# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        range_sum = 0
        def helper(node, l, h):
            nonlocal range_sum
            if not node:
                return
            if l <= node.val <= h:
                range_sum += node.val
            if node.val >= low:
                helper(node.left, l, h)
            if node.val <= high:
                helper(node.right, l, h)
            
        helper(root, low, high)
        return range_sum
