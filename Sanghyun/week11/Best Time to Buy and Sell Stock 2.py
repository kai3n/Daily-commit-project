from typing import List 
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #주식 수익 저장 
        result = 0
        # prices만큼 길이 만큼 반복 
        for i in range(len(prices) - 1):
            # 다을날 주식 가격이 더 크다면 result에 수익 저장 
            if prices[i + 1] > prices[i]:
                result += prices[i + 1] - prices[i]
        # 주식 총 수익 반환 
        return result