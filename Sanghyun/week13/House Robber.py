from typing import List
import collections
class Solution:
    # 훔칠 수 있는 가장 큰 금액 반환
    def rob(self, nums: List[int]) -> int:
        # nums이 없으면 0 반환 
        if not nums:
            return 0
        # nums 2보다 작으면 0번째, 1번째중 큰거 반환 
        if len(nums) <= 2:
            return max(nums)
        # 입력 순서대로 저장하기 위해서 OrderedDict로 선언 
        dp = collections.OrderedDict()
        # 초기값 설정 
        dp[0], dp[1] = nums[0], max(nums[0], nums[1])
        for i in range(2, len(nums)):
            # 옆집 건너 뛰어서 더한 값이랑 비교해서 더 큰 값을 넣어줌 
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
        # 순서가 정해져 있으므로 맨 마지막 item을 pop한 후 가장 큰 금액을 반환 [1]에 존재 
        return dp.popitem()[1]