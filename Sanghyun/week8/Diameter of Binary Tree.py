# 노드 클래스 정의 
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # 직경 초기화 
    longest= 0
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        def dfs(node: TreeNode) -> int:

            # 자식노드의 left, right 노드 끝단 까지 갔을때 없을경우 None이므로 -1을 리턴 
            if not node:
                return -1

            # 자식노트 다음 노드까지 계속 들어감
            left = dfs(node.left)
            right = dfs(node.right)

            # 왼쪽, 오른쪽 상태값에 2를 더해서 거리를 구함. 기존 거리에 누적으로 max 값을 측정
            self.longest = max(self.longest, left + right + 2)

            # 자식 노드에 1 더해서 상태값을 반환
            return max(left, right) + 1
        # dfs 
        dfs(root)
        return self.longest