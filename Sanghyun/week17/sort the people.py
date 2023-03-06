from typing import List
class Solution:
    # 사람 키 순으로 정렬
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        # 사람 키,나이 저장
        people=[]
        # 사람 이름 저장
        answer = []
        # people에 키랑 이름 저장
        for i in range(len(heights)):
            people.append([heights[i],names[i]])
        # 키를 기준으로 정렬
        people.sort(reverse=True)
        # 키 순서대로 이름 저장
        for i in people:
            answer.append(i[1])
        # 정렬된 키 순으로 이름 반환
        return answer