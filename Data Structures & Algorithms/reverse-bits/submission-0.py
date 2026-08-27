class Solution:
    def reverseBits(self, n: int) -> int:
        res=0
        for i in range(32):
            rightmostBit=n&1
            if rightmostBit:
                res+=(2**(31-i))
            n>>=1
        return res

            
        