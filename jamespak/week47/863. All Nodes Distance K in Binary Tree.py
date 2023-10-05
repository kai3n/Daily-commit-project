# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        def dfs(node, parent = None):
            if node:
                node.parent = parent
                dfs(node.left, node)
                dfs(node.right, node)
        dfs(root)
        
        queue = collections.deque([(target, 0)])
        seen = {target}
        while queue:
            if queue[0][1] == k:
                return [node.val for node, _ in queue]
            node, d = queue.popleft()
            for nei in (node.left, node.right, node.parent):
                if nei and nei not in seen:
                    seen.add(nei)
                    queue.append((nei, d+1))
        return []
