# 노드 정의 
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    # 동일한 값 이동 경로 값
    result: int = 0 
    def longestUnivaluePath(self, root: TreeNode) -> int:
        def dfs(node:TreeNode):
            # node가 없으면 0리넡ㄴ
            if node is None:
                return 0
            # dfs로 계속 탐색
            left = dfs(node.left)
            right = dfs(node.right)
            # left가 있고 값이 같으면 같은경로가 1개 있으므로 값 +1갱신
            if node.left and node.left.val == node.val:
                left+=1
            # 없으면 0으로 갣신
            else:
                left =0
            # right가 있고 값이 같으면 같은경로가 1개 있으므로 값 +1갱신
            if node.right and node.right.val == node.val:
                right+=1
            # 없으므로 값갱신 
            else:
                right =0
            # self.result와 left+right 최대값을 갱신 
            self.result = max(self.result,left+right)
            # 자식노드 상태값 중 큰 값 반환 
            return max(left,right)

        dfs(root)
        return self.result