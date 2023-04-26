from typing import List

# 연결 리스트 정의
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        # arr에 head값 다 저장
        p = head
        arr: List = []
        while p:
            arr.append(p.val)
            p = p.next

        # arr 정렬
        arr.sort()

        # head의 연결리스트에 정렬된 arr값 갱신 
        p = head
        for i in range(len(arr)):
            p.val = arr[i]
            p = p.next
        # 정렬된 head 반환
        return head