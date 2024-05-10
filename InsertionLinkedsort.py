# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        sortedList=None
        temp=head
        while temp:
            temp2=temp.next
            sortedList=self.sorts(sortedList,temp)
            temp=temp2
        return sortedList    
    def sorts(self,sortedList,unsortedpart):
        if not sortedList or sortedList.val>=unsortedpart.val:
            unsortedpart.next=sortedList
            return unsortedpart
        else:
            temp=sortedList
            while temp.next and temp.next.val<unsortedpart.val:
                temp=temp.next
            unsortedpart.next=temp.next
            temp.next=unsortedpart
            return sortedList            


        
