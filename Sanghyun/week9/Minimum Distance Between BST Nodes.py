import sys 
# 노드 정의 
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # 이전 노드 값 
    prev = -sys.maxsize
    # 노드간에 가장 작은 차이 반환 
    result = sys.maxsize
    def minDiffInBST(self, root: TreeNode) -> int:
        # 제일 작은 것에서 하나씩 비교 
        if root.left:
            self.minDiffInBST(root.left)
        # 가장 작은 차이 와 현재노드 이전노드 비교해서 최소값 반환 
        self.result = min(self.result,root.val - self.prev)
        # 현재노드 값 이전노드로 저장
        self.prev = root.val 
        if root.right:
            # 왼쪽부터 다 탐색후 오른쪽 탐색시작
            self.minDiffInBST(root.right)
        # 노드간에 가장 작은 차이 값 반환
        return self.result