import collections
# 트리 노드 정의
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def invertTree(self, root: TreeNode) ->TreeNode:
        # 트리노드 queue에 저장
        queue = collections.deque([root])

        while queue:
            # 루트 노드부터 반환
            node = queue.popleft()

            if node:
                # 노드가 있으면 왼쪽이랑 오른쪽 값 바꿈
                node.left, node.right = node.right,node.left
                # 왼쪽 자식노드들도 바껴야 되므로 큐에 저장
                queue.append(node.left)
                queue.append(node.right)
        # 이진 트리 반전해서 반환
        return root