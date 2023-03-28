import heapq
from typing import List


# 연결리스트 정의 
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        # root는 반환
        root = result = ListNode(None)
        # heap 초기화
        heap = []

        # 연결 리스트 루트들을 힙에 저장
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(heap, (lists[i].val, i, lists[i]))

        while heap:
            # 힙에서 추출 후 다음 노드는 다시 저장 
            node = heapq.heappop(heap)
            # 인덱스, 연결리스트 값 할당 
            idx = node[1]
            result.next = node[2]

            result = result.next
            # 다음 노드 있을시 heap에 저장
            if result.next:
                heapq.heappush(heap, (result.next.val, idx, result.next))
        # 정렬 된 리스트 병합해서 반환
        return root.next