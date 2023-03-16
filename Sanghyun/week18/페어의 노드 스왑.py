# 연결리스트 정의 
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 페어 단위로 스왑 
    def swapPairs(self, head: ListNode) -> ListNode:
        cur = head
        while cur and cur.next:
            # 값 교환후 cur 위치갱신 
            cur.val, cur.next.val = cur.next.val, cur.val
            cur = cur.next.next
        # 스왑 한 리스트 반환
        return head