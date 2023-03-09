from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # 자신을 제외한 곱 저장
        answer = []

        p = 1
        for i in range(0, len(nums)):
            # 이전 값 누적으로 곱하면서 answer에 저장
            answer.append(p)
            p = p * nums[i]
        # 포인트 초기화
        p = 1
        for i in range(len(nums) - 1, -1, -1):
            # answer에 p를 곱해주면서 갱신 
            answer[i] = answer[i] * p
            # p는  nums값과 곱해주면서 갱신
            p = p * nums[i]
        # 자신을 제외한 곱 리스트로 반환
        return answer
