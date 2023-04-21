import sys

# 트리 노드정의
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 이전값 저장
    prev = -sys.maxsize
    # 최소값 저장
    result = sys.maxsize

    def minDiffInBST(self, root: TreeNode) -> int:
        # 맨 왼쪽으로 끝까지 탐색
        if root.left:
            self.minDiffInBST(root.left)
        # 이전 노드와 현재 노드 값비교 해서 최소값으로 갱신
        self.result = min(self.result, root.val - self.prev)
        # 이전 값 갱신
        self.prev = root.val
        # 맨 오른쪽 까지 탐색
        if root.right:
            self.minDiffInBST(root.right)
        # 두 노드간 값의 차이가 가장 작은 노드의 값 차이 반환
        return self.result