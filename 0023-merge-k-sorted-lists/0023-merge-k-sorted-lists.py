# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:
    def mergeKLists(self, lists: list[ListNode | None]) -> ListNode | None:
        min_heap=[]
        count=0
        for node in lists:
            if node:
                heapq.heappush(min_heap,(node.val,count,node))
                count+=1
        dummy=ListNode(0)
        tail=dummy
        while min_heap:
            _,_,smallest=heapq.heappop(min_heap)
            tail.next=smallest
            tail=tail.next
            if smallest.next:
                heapq.heappush(min_heap,(smallest.next.val,count,smallest.next))
                count+=1
        return dummy.next


        