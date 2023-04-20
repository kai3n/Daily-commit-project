# 트리노드 정의 
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # 범위 합 계산
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        def dfs(node:TreeNode):
            # node없으면 0반환
            if not node:
                return 0
            # node 값이 low보다 작을때 오른쪽 탐색
            if node.val < low:
                return dfs(node.right)
            # node 값이 high보다 클때 왼쪽 탐색
            elif node.val > high:
                return dfs(node.left)
            # node에 게속 값을 더해서 갱신
            return node.val + dfs(node.left) + dfs(node.right)
        # 이진 탐색 트리 합의 범위 계산해서 반환
        return dfs(root)