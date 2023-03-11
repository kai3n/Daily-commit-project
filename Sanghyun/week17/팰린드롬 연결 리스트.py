# 연결리스트 선언
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        q = [] 
        # head가 없으면 True반환
        if not head:
            return True

        node = head
        # 값이 잇으면 q에 저장 후 노드 갱신
        while node is not None:
            q.append(node.val)
            node = node.next

        # 팰린드롬 안될시 False반환
        while len(q) > 1:
            if q.pop(0) != q.pop():
                return False
        # 팰린드롬 가능하면 True반환
        return True