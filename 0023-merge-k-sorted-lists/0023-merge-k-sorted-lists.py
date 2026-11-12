# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoSortedLists(self,l1:ListNode | None, l2:ListNode | None)-> ListNode | None:
        if not l1:
            return l2
        if not l2:
            return l1
        if l1.val<=l2.val:
            l1.next=self.mergeTwoSortedLists(l1.next,l2)
            return l1
        else:
            l2.next=self.mergeTwoSortedLists(l2.next,l1)
            return l2
    def partitionAndMerge(self, start: int, end: int, lists: list[ListNode | None]) -> ListNode | None:
        if start==end:
            return lists[start]
        if start>end:
            return None
        mid=start+(end-start)//2
        l1=self.partitionAndMerge(start,mid,lists)
        l2=self.partitionAndMerge(mid+1,end,lists)

        return self.mergeTwoSortedLists(l1,l2)

    def mergeKLists(self, lists: list[ListNode | None]) -> ListNode | None:
        n=len(lists)
        if n==0:
            return None
        return self.partitionAndMerge(0,n-1,lists)