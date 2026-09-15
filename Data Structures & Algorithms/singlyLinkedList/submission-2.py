
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    
    def __init__(self):
        self.head=None
   
    def get(self, i: int) -> int:
        c=0
        temp=self.head
        while(temp and c<i):
            temp=temp.next
            c+=1
        if temp:
            return temp.data

        return -1     

    def insertHead(self, val: int) -> None:
        newNode=Node(val)
        newNode.next=self.head
        self.head=newNode
    

    def insertTail(self, val: int) -> None:
        newNode=Node(val)
        if not self.head:
            self.head=newNode
            return
        temp=self.head
        while(temp.next):
            temp=temp.next
        temp.next=newNode
        

    def remove(self, index: int) -> bool:
        if not self.head:
            return False
        temp=self.head
        c=0
        if index==0:
            self.head=self.head.next
            return True
        
        while(temp and c<index-1):
            temp=temp.next
            c+=1
        if not temp or not temp.next:
            return False
        temp.next=temp.next.next
        return True
        
    def getValues(self) -> List[int]:
        res=[]
        if not self.head:
            return res
        temp=self.head
        while(temp):
            res.append(temp.data)
            temp=temp.next
        return res        
