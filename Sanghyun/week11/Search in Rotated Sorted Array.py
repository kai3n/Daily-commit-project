from typing import List
class Solution:
    # 회전 정열 된 것 검색 
    def search(self, nums: List[int], target: int) -> int:
        # nums값이 없으면 -1리턴 
        if not nums:
            return -1 
        # 정렬되어 있으므로 left는 왼쪽인덱스 right는 오른쪽 인덱스 설정 
        left , right = 0, len(nums)-1
        # left가 right 작으면 계속 반복
        while left < right:
            # 중앙값 계속 갱신 
            mid = left + (right - left) //2 
            # nums[mid]가 nums[right]보다 크면 회전되어 있으므로 left 갱신 
            if nums[mid] > nums[right]:
                left = mid +1
            #  아니면 제대로 정렬되어 있으므로 right 갱신
            else:
                right = mid 
        # 최소값 인덱스를 피벗으로 지정 
        pivot = left 
        # 정렬되어 있으므로 left는 왼쪽인덱스 right는 오른쪽 인덱스 설정
        left , right = 0, len(nums)-1
        # left가 right보다 작거나 같을때 반복 
        while left <= right:
            # 중앙값 갱신 
            mid = left + (right - left) //2
            # 최소값 pivot을 구해놨으므로 mid를 더해서 mid_pivot구함 
            mid_pivot = (mid + pivot) % len(nums)
            # target보다 작을떄는 left를 갱신 
            if nums[mid_pivot] < target:
                left = mid +1
            #  target보다 클때는 right갱신 
            elif nums[mid_pivot] > target:
                right = mid -1
            # 위 두 경우가 아닐경우 target값이므로 반환 
            else:
                return mid_pivot
        # target이 없을경우 -1 반환
        return -1