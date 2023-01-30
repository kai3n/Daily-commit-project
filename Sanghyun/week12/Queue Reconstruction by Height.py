from typing import List
import heapq
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        # 우선순위 큐로 구현 
        heap = []
        for person in people:
            # 최대힙을 위해서 음수 사용
            heapq.heappush(heap, (-person[0], person[1]))
        # 결과 반환 
        result = []
        # heap 없을때까지 반복 
        while heap:
            # 키가 큰순으로 pop됨 
            person = heapq.heappop(heap)
            # person[1]은 인덱스로 사용해서 person[1] 인덱스에 삽입 
            result.insert(person[1], [-person[0], person[1]])
        # 앞에 자신의 키 이상인 사람들 정렬 한 값 반환 
        return result