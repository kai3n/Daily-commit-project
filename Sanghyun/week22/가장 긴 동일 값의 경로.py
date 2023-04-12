class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    result = 0

    def longestUnivaluePath(self, root:TreeNode) -> int:
        
        def dfs(node):
            # 노드 없을떄 0 값 반환
            if node is None:
                return 0
            # 왼쪽, 오른쪽 탐색 
            left = dfs(node.left)
            right = dfs(node.right)
            # 현재 노드랑 왼쪽 자식노드 값이 같으면 left값 갱신
            if node.left and node.left.val == node.val:
                left+=1
            else:
                left =0
            # 현재 노드랑 오른쪽 자식노드 값이 같으면 right값 갱신
            if node.right and node.right.val == node.val:
                right+=1
            else:
                right =0
            # result값이랑 left right 합쳐서 동일값 경로 길이 갱신
            self.result = max(self.result,left+right)
            return max(left,right)

        dfs(root)
        # 가장 긴 동일 값 경로 길이 반환
        return self.result