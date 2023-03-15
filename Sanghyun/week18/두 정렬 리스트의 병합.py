# 연결리스트
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 두 정렬 리스트병합 
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # l1,l2 값 비교 후 l1이 크면 l2랑 값 교환 
        if (not l1) or (l2 and l1.val > l2.val):
            l1, l2 = l2, l1
        if l1:
            #재귀로 다음 값들 병합하면서 정렬 
            l1.next = self.mergeTwoLists(l1.next, l2)
        # 정렬된 리스트 반환
        return l1
    