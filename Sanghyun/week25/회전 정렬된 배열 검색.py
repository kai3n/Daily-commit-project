from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # 예외 처리
        if not nums:
            return -1

        # 투포인트로 최솟값 찾ㅣ 
        left, right = 0, len(nums) - 1
        while left < right:
            # mid값 갱신
            mid = left + (right - left) // 2

            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        # 최솟값 pivot으로 설ㅓ 
        pivot = left
        # 피벗 기준으로 이진 검색
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            # 탐색 할 인덱스 갱신
            mid_pivot = (mid + pivot) % len(nums)

            if nums[mid_pivot] < target:
                left = mid + 1
            elif nums[mid_pivot] > target:
                right = mid - 1
            else:
                return mid_pivot
        return -1