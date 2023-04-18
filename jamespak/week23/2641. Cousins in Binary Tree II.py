# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        current_level_sum = root.val
        q = [root]
        while q:
            next_level, next_level_sum = [], 0
            for node in q:
                node.val = current_level_sum - node.val
                for kid in node.left, node.right:
                    if kid:
                        next_level.append(kid)
                        next_level_sum += kid.val        
                if node.left and node.right:
                    sm = node.left.val + node.right.val
                    node.left.val = node.right.val = sm
            q, current_level_sum = next_level, next_level_sum
        return root
