class Solution:
    def hammingWeight(self, n: int) -> int:
        c=0
        while n:
            c+=n%2
            n=n//2
        return c
        