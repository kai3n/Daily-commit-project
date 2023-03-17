# 연결리스트 정의 
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        # 없으면 None 반환
        if head is None:
            return None
        
        # 홀수 짝수 헤드 설정 
        odd = head
        even = head.next
        even_head = head.next

        # 홀수 짝수 노드 처리 
        while even and even.next:
            odd.next, even.next = odd.next.next, even.next.next
            odd, even = odd.next, even.next

        # 홀수 노드 마지막에 짝수 노드 연결
        odd.next = even_head
        # 홀짝 연결리스트 반환
        return head