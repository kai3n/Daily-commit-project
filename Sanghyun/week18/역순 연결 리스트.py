# 연결 리스트 정의
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 역순 연결리스트 
    def reverseList(self, head: ListNode) -> ListNode:
        # 변수 초기화 
        node, prev = head, None
        # 노드 있으면 반복
        while node:
            # prev에 역순으로 하나씩 저장
            next, node.next = node.next, prev
            prev, node = node, next
        # 역순 연결리스트 반환
        return prev