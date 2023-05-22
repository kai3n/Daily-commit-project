# Definition for a rope tree node.
# class RopeTreeNode(object):
#     def __init__(self, len=0, val="", left=None, right=None):
#         self.len = len
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getKthCharacter(self, root: Optional[object], k: int) -> str:
        """
        :type root: Optional[RopeTreeNode]
        """
        self.res = []
        def helper(root, res):
            if root:
                if root.len == 0:
                    res.append(root.val)
                helper(root.left, res)
                helper(root.right, res)
        helper(root, self.res)
        return "".join(self.res)[k-1]
