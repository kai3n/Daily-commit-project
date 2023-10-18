# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        ListNode.__eq__ = lambda a, b: a.val == b.val
        ListNode.__lt__ = lambda a, b: a.val < b.val

        head = point = ListNode(0)
        h = []
        for l in lists:
            if l:
                heapq.heappush(h, [l.val, l])
                
        while h:
            val, node = heapq.heappop(h)
            point.next = ListNode(val)
            point = point.next
            node = node.next
            if node:
                heapq.heappush(h, [node.val, node])
        return head.next
