# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:

        def reverse(n: ListNode) -> ListNode:
            tail = None
            while n:
                tmp = n.next
                n.next = tail
                tail = n
                n = tmp
            return tail

        cur = tail = reverse(head)
        cur_max = cur.val
        while cur.next:
            if cur.next.val < cur_max:
                cur.next = cur.next.next
            else:
                cur = cur.next
                cur_max = cur.val
        return reverse(tail)
