# 트리노드 정의
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def check(root):
            # root없을떄 0반환
            if not root:
                return 0 
            # 왼쪽 오른쪽 탐색
            left = check(root.left)
            right = check(root.right)   
            # 균형 이진트리가 아닐때 -1반환
            if left == -1 or right == -1 or abs(left-right) > 1:
                return -1 
            # 깊이 반환
            return max(left,right) + 1
        # 균형이진 트리가 아닐때 False, 균형이진 트리일때 True 반환
        return check(root) != -1 