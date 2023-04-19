class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # 노드값 갱신 value값
    val = 0
    def bstToGst(self, root: TreeNode) -> TreeNode:
        # root가 존재 할때
        if root:
            # 제일 큰값부터 탐색 후 값 갱신 그 후 왼쪽 탐색해서 값 갱신함
            self.bstToGst(root.right)
            self.val += root.val
            root.val = self.val
            self.bstToGst(root.left)
        # 이진 트리에서 더 큰수들 합계 트리를 반환
        return root       