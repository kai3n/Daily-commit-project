from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        result = 0
        for i in range(len(prices) - 1):
            # 다음날 값이 오를떄마다 갱신
            if prices[i + 1] > prices[i]:
                result += prices[i + 1] - prices[i]
        # 총 수익금액 반환
        return result