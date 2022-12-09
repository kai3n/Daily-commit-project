class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        self.res = 0

        def helper(root, cur_max, cur_min):
            if not root:
                return
            self.res = max(self.res, abs(cur_max - root.val), abs(cur_min - root.val))
            cur_max = max(cur_max, root.val)
            cur_min = min(cur_min, root.val)
            helper(root.left, cur_max, cur_min)
            helper(root.right, cur_max, cur_min)
        
        helper(root, root.val, root.val)
        return self.res
