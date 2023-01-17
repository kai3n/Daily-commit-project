# 연결리스트 노드 정의 
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    # 삽입 정렬로 정렬 
    def insertionSortList(self, head: ListNode) -> ListNode:
        # cur은 정렬을 끝낸 연결리스트, parent는 루트노드를 계속 가르킴
        cur = parent =ListNode(None)
        # head가 None이면 비교가 끝 
        while head:
            # 정렬을 끝내 노드가 head의 값보다 작으면 cur을 다음으로 계속 이동 
            while cur.next and cur.next.val < head.val:
                cur = cur.next

            # cur 다음을 head로 가르키고 cur 다음을 head 다음으로 가리키고 head에 head다음 가리켜 계속 연결 시킨다 
            cur.next, head.next, head = head, cur.next, head.next
            # 다시 처음으로 되돌아가며 위 과정을 반복 
            cur = parent 
        # 삽입 정렬로 정렬된 리스트 반환
        return cur.next