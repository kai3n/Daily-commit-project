from typing import List
# 노드 정의 
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    # 오름차순으로 정렬된 배열을 높이 균형 이진트리로 변환 
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        # nums 없으면 None으로 반환 
        if not nums:
            return None
        # nums의 중간값 저장 
        mid = len(nums) // 2 
        # nums의 중간값을 노드로 설정
        node = TreeNode(nums[mid])
        # 왼쪽 자식 노드를 재귀 호출로 계속 처리
        node.left = self.sortedArrayToBST(nums[:mid])
        # 오른쪽 자식 노드를 재귀 호출로 계속 처리 
        node.right = self.sortedArrayToBST(nums[mid+1:])
        # 이진 트리 반환 
        return node