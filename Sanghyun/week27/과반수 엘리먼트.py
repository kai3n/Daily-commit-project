from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # 정렬후 중간 인덱스 반환하면 과반수이상 엘리먼트임 
        return sorted(nums)[len(nums) // 2]