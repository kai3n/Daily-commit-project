from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # 순열 결과값 저장 
        results = []
        prev_elements = []

        def dfs(elements):
            # 노드 마지막일 경우 results에 추가 [:]는 참조관계를 갖지 안도록 처리 
            if len(elements) == 0:
                results.append(prev_elements[:])

            for e in elements:
                # 한개씩 제거후 탐색
                next_elements = elements[:]
                next_elements.remove(e)
                # 이전 노드에 값을 추가 
                prev_elements.append(e)
                dfs(next_elements)
                # 탐색이 다 끝나면 prev_elements를 []로 만들어줌
                prev_elements.pop()
        # 순열 계산
        dfs(nums)
        # 순열 반환
        return results