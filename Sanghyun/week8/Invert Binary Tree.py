import collections
# 노드 정의 
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    # 이진 트리 반전 시키기 
    def invertTree(self, root: TreeNode) ->TreeNode:
        # root를 데큐에 저장 
        queue = collections.deque([root])

        # queue존재 할때 반복 
        while queue:
            # 루트 노드부터 하나씩 출력 
            node = queue.popleft()
            if node:
                # node가 있으면 왼쪽이랑 오른쪽 값 변경
                node.left, node.right = node.right,node.left
                #queue에 바꿔서 계속 저장 
                queue.append(node.left)
                queue.append(node.right)
        # 이진트리 루트 노드를 기준으로 반전시켜서 반환
        return root