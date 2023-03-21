from typing import List

class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        # 언제 기온이 더 높아지는지 결과값 저장
        answer = [0] * len(T)
        stack = []
        for i, cur in enumerate(T):
            # 현재 온도가 스택에 있는 온도보다 높으면 값 계산
            while stack and cur > T[stack[-1]]:
                last = stack.pop()
                answer[last] = i - last
            # 스택에 인덱스 추가
            stack.append(i)
        # 기온이 더 높아지는 인덱스들 반환
        return answer