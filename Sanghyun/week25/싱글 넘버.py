from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # 값이 한개 인거출력
        result = 0 
        for num in nums:
            # ^ 연산으로 값이 2개 나면 0으로 상쇄됨 
            result ^= num
        #한개 값 출력 
        return result 