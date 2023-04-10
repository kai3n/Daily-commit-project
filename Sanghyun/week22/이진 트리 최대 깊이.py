import collections

# 트리 노드 정의
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        # 노드 없으면 0 반환
        if root is None:
            return 0
        # 데크로 저장
        queue = collections.deque([root])
        # 깊이 저장
        depth = 0
        
        while queue:
            # 큐 있으면 깊이 갱신
            depth += 1

            for _ in range(len(queue)):
                # 루트 노드 저장
                cur_root = queue.popleft()
                # 왼쪽 있으면 큐에 추가
                if cur_root.left:
                    queue.append(cur_root.left)
                # 오른쪽 있으면 큐에 추가
                if cur_root.right:
                    queue.append(cur_root.right)
        # 깊이 반환
        return depth