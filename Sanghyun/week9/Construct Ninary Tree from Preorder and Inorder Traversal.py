from typing import List
# 노드 정의 
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # 전위 순회, 중위 순회로 이진 트리 구축 
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        # 중위 순회 결과가 있을떄 
        if inorder:
            # 전위 순회의 제일 처음 인덱스를 가지고 와서 중위 순회를 분할 시키는 역할
            index = inorder.index(preorder.pop(0))
            # 값을 현재 노드로 정의 
            node = TreeNode(inorder[index])
            # 중위 순회 결과를 왼쪽으로 쪼개고 오른쪽으로 쪼개서 계속 재귀 호출하면 트리 구조로 구성 
            node.left = self.buildTree(preorder,inorder[0:index])
            node.right = self.buildTree(preorder,inorder[index+1:])
            # 이진 트리 반환 
            return node