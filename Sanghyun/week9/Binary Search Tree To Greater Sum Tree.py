# 노드 정의
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    # 자신보다 큰 노드 합 저장
    val = 0
    # 현재 노드 보다 큰 노드들 합친 값으로 갱신
    def bstToGst(self, root: TreeNode) -> TreeNode:
        if root:
            # 우선 노드가 존재하면 이진 트리는 맨 오른쪽이 가장 큰수이기 때문에 맨 오른쪽 자식노드부터 탐색 
            self.bstToGst(root.right)
            # 노드 값을 계속 갱신 
            self.val += root.val
            # 노드 값 변경 
            root.val = self.val
            # 오른쪽 끝나면 맨쪽 탐색후 계속 누적 
            self.bstToGst(root.left)
        # 자기 자신보다 큰 노드들의 합으로 갱신한 TreeNode륿 반환
        return root