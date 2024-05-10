# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left==right:
            return head
        curr=head
        prev=None
        while left>1:
            prev=curr
            curr=curr.next
            left-=1
            right-=1
        tail=curr
        nex=prev
        while right>0:
            nexs=curr.next
            curr.next=prev   
            prev=curr
            curr=nexs
            right-=1
        if nex:
            nex.next=prev
        else:
            head=prev
        tail.next=curr
        return head                 
            
        
