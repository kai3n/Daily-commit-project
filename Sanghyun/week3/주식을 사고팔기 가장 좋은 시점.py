from typing import List
import sys

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #이익을 저장
        profit = 0 
        # 초깃값을 최대값으로 설정 
        min_price = sys.maxsize 
        # 주식 가격 반복 
        for price in prices :
            # 초깃값을 최대값으로 설정 했기 떄문에 가격에 따라서 최솟값 저장 
            min_price = min(min_price,price)
            # 이익이 더 클 떄 비교 
            profit = max(profit, price - min_price)
        # 최대 이익을 산출 
        return profit