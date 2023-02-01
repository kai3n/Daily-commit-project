from typing import List
import collections
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # 값이 없을때 default선언할수 있도록 하기위해서 collections 사용 
        counts = collections.defaultdict(int)
        # nums에 있는 값들 반복 
        for num in nums:
            # counts에 키 값이 없다면 nums에서 num갯수를 찾아서 저장시켜놓음 
            if counts[num] == 0:
                counts[num] = nums.count(num)
            # counts에 저장한 값이 nums의 과반수 이상이라면 반환 
            if counts[num] > len(nums)//2:
                return num