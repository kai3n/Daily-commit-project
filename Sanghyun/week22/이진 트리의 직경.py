class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    longest= 0
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        def dfs(node: TreeNode) -> int:

            # 리프노드가 없을때 -1 반환
            if not node:
                return -1

            # 리프노드 다음 자식까지 탐색
            left = dfs(node.left)
            right = dfs(node.right)

            # 기존 거리에 누적해서 최대값 갱신
            self.longest = max(self.longest, left + right + 2)

            # 자식 노드에 +1 해서 갱신
            return max(left, right) + 1
        dfs(root)
        # 트리 노드 직경반환
        return self.longest