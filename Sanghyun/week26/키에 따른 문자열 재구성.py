from typing import List
import heapq

class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        heap = []
        # 키역순으로 head에 저장 
        for person in people:
            heapq.heappush(heap, (-person[0], person[1]))

        result = []
        while heap:
            # 키 큰순으로 pop도ㅣㅁ 
            person = heapq.heappop(heap)
            # person[1] 인덱스에 [-person[0],person[1]] 삽입
            result.insert(person[1], [-person[0], person[1]])
        # 올바르게 정렬된 대기열 반환
        return result