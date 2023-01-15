# 연결리스트 정의
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # 연결리스트 정렬 내장함수 사용 
    def sortList(self, head: ListNode) -> ListNode:
        # 연결리스트 저장 
        p = head 
        # 리스트로 저장 
        store = [] 
        # 노드가 있으면 반복 
        while p:
            # 노드값 리스트에 저장 
            store.append(p.val)
            # 다음 노드로 갱신 
            p = p.next
        # 리스트 값들 정렬
        store.sort()

        p = head
        # 리스트 크기만큼 반복 
        for i in range(len(store)):
            # 리스트에 있는 값 노드에 갱신 
            p.val = store[i]
            # 다음 노드로 갱신 
            p=p.next
        # 정렬된 연결리스트 반환 
        return head