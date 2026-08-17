# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        n1=0
        n2=0

        p1=l1
        p2=l2

        while(p1):
            n1+=1
            p1=p1.next
        while(p2):
            n2+=1
            p2=p2.next
        
        p1=l1
        p2=l2
        c=0
        res1=0
        
        while(c<n1):
            res1+=(p1.val)*(10**c)
            c+=1
            p1=p1.next
        c=0
        res2=0
        while(c<n2):
            res2+=(p2.val)*(10**c)
            c+=1
            p2=p2.next

        res=res1+res2
        dummy=ListNode()
        curr=dummy
        if res==0:
            return ListNode(0)
        while(res):
            curr.next=ListNode(res%10)
            res=res//10
            curr=curr.next
        return dummy.next
        