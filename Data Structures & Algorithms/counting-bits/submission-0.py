class Solution:
    def countBits(self, n: int) -> List[int]:
        res,x=[],0
        while(x<=n):
            res.append(self.setBits(x))
            x+=1
        return res
    
    def setBits(self,n):
        c=0
        while(n>0):
            c+=n&1
            n>>=1
        return c