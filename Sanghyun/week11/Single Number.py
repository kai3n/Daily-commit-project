from typing import List 
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # 값이 한개인거 담는 변수 
        result = 0 
        for num in nums:
            # XOR 2번 하면 값이 0이 되므로 결국 1개의 엘리먼트의 값만 남게됨 
            result ^= num
        # 값이 한개만 반환 
        return result