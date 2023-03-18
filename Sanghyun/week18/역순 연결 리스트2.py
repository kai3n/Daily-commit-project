# 연결 리스트 정의 
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 부분 역순 연결리스트 
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        # head값이 없거나 인덱스가 같다면 head 반환
        if not head or m == n:
            return head
        # 반환 해줄 값 초기화 
        root = start = ListNode(None)
        root.next = head
        # start, end값 초기화 
        for _ in range(m - 1):
            start = start.next
        end = start.next

        # m n 사이 차례대로 리스트 뒤집기 
        for _ in range(n - m):
            tmp = start.next
            start.next = end.next
            end.next = end.next.next
            start.next.next = tmp 
        # m n 사이 역순 연결 리스트 반환 
        return root.next