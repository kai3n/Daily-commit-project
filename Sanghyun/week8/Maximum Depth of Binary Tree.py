import collections
# 노드 클래스 정의 
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        # root가 없으면 종료 
        if root is None :
            return 0 
        # 큐 선언 
        queue = collections.deque([root])
        # 깊이 0으로 초기화 
        depth =0 
        # 큐가 있으면 반복 
        while queue :
            # 깊이 큐가 있으므로 깊이 +1 갱신 
            depth +=1
            # 큐 길이만큼 반복 
            for _ in range(len(queue)):
                # 하나씩 꺼내면서 확인
                cur_root =queue.popleft()
                # 자식노드가 있으면 자식노드 추가
                if cur_root.left :
                    queue.append(cur_root.left)
                # 자식노드가 있으면 자식노드 추가 
                if cur_root.right:
                    queue.append(cur_root.right)
        # 트리 최대 깊이 반환 
        return depth