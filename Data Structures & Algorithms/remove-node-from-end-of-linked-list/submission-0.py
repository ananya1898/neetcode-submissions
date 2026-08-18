# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return
        dummy=ListNode()
        dummy.next=head
        first=dummy
        second=dummy
        i=0
        while(i<=n):
            if not first:
                return
            first=first.next
            i+=1
        
        while(first):
            second=second.next
            first=first.next

        second.next=second.next.next

        return dummy.next
        