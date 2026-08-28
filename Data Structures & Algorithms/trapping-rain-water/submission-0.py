class Solution:
    def trap(self, height: List[int]) -> int:
        lmax=[0]*len(height)
        rmax=[0]*len(height)
        curr=0
        for i in range(len(height)):
            curr=max(height[i],curr)
            lmax[i]=curr
        curr=0
        for i in range(len(height)-1,-1,-1):
            curr=max(height[i],curr)
            rmax[i]=curr

        res=0
        for i in range(len(height)):
            curr=min(lmax[i],rmax[i])-height[i]
            if curr>0:
                res+=curr
                res=max(res,curr)
 
        return res



            
        