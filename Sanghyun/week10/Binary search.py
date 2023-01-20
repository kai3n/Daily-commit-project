from typing import List

class Solution:
    # logn 복잡도로 target값 인덱스 출력
    def search(self, nums: List[int], target: int) -> int:
        # 투포인트로 left는 0으로 right는 맨마지막 인덱스를 가리키게 초기화 
        left,right = 0, len(nums)-1
        # left가 right보다 작거나 같으면 계속 반복 
        while left <= right:
            # left와 right 중간 값 
            mid = (left + right)//2
            # nums의 mid인덱스 값이 target보다 작으면 왼쪽은 다 작으므로 오른쪽만 탐색하면 됨 따라서 left값 mid +1로 갱신  
            if nums[mid] <target:
                left = mid +1
            # nums의 mid인덱스 값이 target보다 크면 오른쪽은 크므로 왼쪽만 탐색하면 됨 따라서 right값 mid -1로 갱신
            elif nums[mid] > target:
                right = mid-1
            # 위 두 경우에 해당이 안된다면 중간인덱스가 target임 
            else:
                return mid
        # 만약 target이 nums에 존재하지 않는다면 -1 반환 
        return -1