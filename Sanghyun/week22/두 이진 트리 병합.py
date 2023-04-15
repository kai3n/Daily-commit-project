# 트리 노드 정의
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # 두개의 트리 병합
    def mergeTrees(self, root1:TreeNode, root2: TreeNode) -> TreeNode:
        # 둘다 존재시 병합 진행
        if root1 and root2:
            # 노드를 생성 
            node = TreeNode(root1.val+root2.val)
            # 왼쪽 노드 병합
            node.left = self.mergeTrees(root1.left,root2.left)
            # 오른쪽 노드 병합
            node.right = self.mergeTrees(root1.right,root2.right)
            # 병합된 노드 반환
            return node 
        # 한개만 존재시 트리 루트 노드 반환
        else:
            return root1 or root2