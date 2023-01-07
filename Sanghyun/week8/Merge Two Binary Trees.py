# 노드 정의 
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def mergeTrees(self, root1:TreeNode, root2: TreeNode) -> TreeNode:
        # 두개의 노드가 있을때 병합
        if root1 and root2:
            # 루트 노드 값을 합쳐서 저장
            node = TreeNode(root1.val+root2.val)
            # 두개의 노드 왼쪽 자식노드 합치기
            node.left = self.mergeTrees(root1.left,root2.left)
            # 두개의 노드 오른쪽 자식 노드 합치기
            node.right = self.mergeTrees(root1.right,root2.right)
            # 노드 반환 
            return node
        # 한개만 있을때는 한개만 반환 
        else:
            return root1 or root2