from typing import List

class Solution:
    # 최대 수익 반환
    def maxProfit(self, prices: List[int]) -> int:
        # 초기값 설정
        max_price = 0

        for i, v in enumerate(prices):
            for j in range(i, len(prices)):
                # 범위내에서 최대값되는거 갱신 시켜서 최대수익 구현
                max_price = max(prices[j] - v, max_price)
        # 최대 수익 반환
        return max_price