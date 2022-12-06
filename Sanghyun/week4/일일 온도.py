from typing import List
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # 리스트 길이만큼 값을 0으로 갱신 
        answer = [0] * len(temperatures)
        stack =[] 
        # index와 현재 온도값 
        for index , value in enumerate(temperatures):
            # 스택이 존재하거나 현재 값이 이전 온도보다 높을때 반복 
            while stack and value > temperatures[stack[-1]]:
                # 온도가 높을떄 index를 값을 저장
                last = stack.pop()
                 # 다음 높은 날씨가 몇일 더 기다려야되는지 해당인덱스에 저장
                answer[last] = index - last
            # stack이 없거나 현재 온도가 과거 보다 더 클때 스택에 추가
            stack.append(index)
        # 더 따뜻한 날씨를 몇일 기다려야되는지 리스트로 반환

        return answer 