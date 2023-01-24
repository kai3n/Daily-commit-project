from typing import List
class Solution:
    # 두 수의 합  
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # 투포인트 사용 
        left, right = 0, len(numbers)-1
        # 인덱스가 같지 않으면 계속 반복 
        while not left == right:
            #두 수의 합이 target보다 작으면 left인덱스보다 큰값으로 갱신 
            if numbers[left] + numbers[right] < target:
                left += 1 
            #두 수의 합이 target보다 크며ㄴ right인덱스보다 작은값으로 갱신 
            elif numbers[left]+ numbers[right] > target:
                right -=1
            #위 경우가 아면 target이므로 인덱스 반환 
            else:
                return [left+1,right+1]