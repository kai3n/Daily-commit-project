# 노트 정의 
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # 균형 이진트리 탐색 
    def isBalanced(self, root: TreeNode) -> bool:
        # 균형 이진트리 인지 확인 
        def check(root):
            # 자식노드가 없다면 0을 리턴 
            if not root:
                return 0 
            # 자식노드가 있으므로 왼쪽, 오른쪽 탐색 
            left = check(root.left)
            right = check(root.right)
            # -1은 노드를 기준으로 균형이 1이상 차이 난다는 의미이므로 -1리턴, left와 right차이가 1초과해도 균형이 안맞으므로 -1리턴
            if left == -1 or right == -1 or abs(left-right) > 1:
                return -1 
            # 균형이 맞으면 노드는 left,right중 높은 값에 +1을 해서 갱신 
            return max(left,right) + 1
        # 균형 이진트리를 체크했는데 노드가 -1이 아니면 균형이 맞으므로 True반환, 아니면 False반환 
        return check(root) != -1