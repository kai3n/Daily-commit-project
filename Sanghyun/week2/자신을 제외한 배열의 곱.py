from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # 결과를 반환하는 리스트 
        result =[]
        
        p=1
        # 리스트 갯수만큼 반복  (왼쪽 곱셈)
        for i in range(0,len(nums)):
            #   [1,2,3,4] -> [1,1,2,6] 마지막 값을 빼고 곱해서 리스트에 추가 해준다 
            result.append(p)
            p = nums[i]*p
    
        p = 1 
        # 리스트 갯수만큼 반복 (오른쪽 곱셈)
        for i in range(len(nums)-1 ,0-1,-1):
            # 위 왼쪽 곱셈 나온 값들을 [1,1,2,6] 인덱스 3부터~ 0까지 곱해서 p를 갱신해준다 
            result[i] = result[i] * p
            p = p*nums[i]
            # 위 for이 다 끝나면 자신을 제외하고 배열곱을 반환해줌 
            
        return result