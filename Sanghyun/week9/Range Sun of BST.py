# 노드 정의 
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # 이진 탐색 트리 합의 범위 
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        # dfs 가지치기로 노드 탐색
        def dfs(node:TreeNode):
            # 노드 없으면 0 반환 
            if not node:
                return 0
            # low보다 작을때는 검색할 필요가 없으므로 dfs 오른쪽 탐색 
            if node.val < low:
                return dfs(node.right)
            # high보다 클때는 검색해야 하므로 dfs 왼쪽 탐색 
            elif node.val > high:
                return dfs(node.left)
            # 사이값들 리턴해서 다 합하기 
            return node.val + dfs(node.left) + dfs(node.right)
        # 이진 탐색 트리 반환 
        return dfs(root)