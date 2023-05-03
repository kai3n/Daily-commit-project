from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # 투포인트 사용
        left, right = 0, len(numbers)-1
        # 오른쪽, 왼쪽으로 한칸씩 이동 후 갱신
        while not left == right:
            # target값 보다 작으면 left 값 갱신
            if numbers[left] + numbers[right] < target:
                left += 1 
            # target값 보다 크면 right 값 갱신
            elif numbers[left]+ numbers[right] > target:
                right -=1
            # 같으면 인덱스 반환
            else:
                return [left+1,right+1]
        
        
