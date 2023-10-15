# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        self.closest = root.val
        def helper(root, target):
            if root:
                if abs(target - root.val) < abs(target - self.closest):
                    self.closest = root.val
                if root.val > target:
                    helper(root.left, target)
                else:
                    helper(root.right, target)
                
        helper(root, target)
        return self.closest
        
