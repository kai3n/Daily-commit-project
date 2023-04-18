from typing import List
# 트리노드 정의 
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    # 정렬된 이진트리 반환
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        # nums이 없으먼 None반환
        if not nums:
            return None
        # 루트 노드 인덱스 값
        mid = len(nums) // 2 
        # 루트 노드 설정 
        node = TreeNode(nums[mid])
        # 루트 노드 자식노드 값 설정 
        node.left = self.sortedArrayToBST(nums[:mid])
        node.right = self.sortedArrayToBST(nums[mid+1:])
        # 정렬된 이진 트리 반환
        return node