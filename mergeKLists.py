# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap=[]
        for u in lists:
            temp=u
            while temp:
                heapq.heappush(heap,temp.val)
                temp=temp.next
        newlist=ListNode(0)
        curr=newlist
        while heap:
            curr.next=ListNode(heapq.heappop(heap))
            curr=curr.next
        return newlist.next             
           
        
