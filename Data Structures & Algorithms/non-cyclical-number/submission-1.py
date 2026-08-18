class Solution:
    def isHappy(self, n: int) -> bool:
        appeared=set()
        while(True):
            n=self.sumOfSquares(n)
            if n==1:
                return True
            if n in appeared:
                return False
            appeared.add(n)

    def sumOfSquares(self,n):
        sum=0
        while(n>0):
            sum+=(n%10)**2
            n=n//10
        return sum