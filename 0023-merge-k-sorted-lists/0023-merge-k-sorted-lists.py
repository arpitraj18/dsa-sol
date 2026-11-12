# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:
    def mergeKLists(self, lists: list[ListNode | None]) -> ListNode | None:
        min_heap=[]
        for i,node in enumerate(lists):
            if node is not None:
                heapq.heappush(min_heap,(node.val,i,node))
        if not min_heap:
            return None
        _,i,head=heapq.heappop(min_heap)
        if head.next is not None:
            heapq.heappush(min_heap,(head.next.val,i,head.next))
        tail=head
        while min_heap:
            _,i,curr=heapq.heappop(min_heap)
            tail.next=curr
            tail=tail.next
            if curr.next is not None:
                heapq.heappush(min_heap, (curr.next.val, i, curr.next))
                
        return head
        