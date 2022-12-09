class ListNode:
    def __init__(self, val=0, next=None):
        # 값 매개변수 
        self.val = val
        # 다음 노드 변수
        self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # 현재 노드와 , 역으로 넣을 노드 변수 선언
        node , prev = head , None
        # 노드가 존재하면 
        while node :
            # node.next를 node로 바꾸고 prev에 node를 추가 하면서 역순을 만듬 
            next , node.next = node.next, prev 
            prev , node = node , next 
        # 연결리스트 역순으로 반환 
        return prev