class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l=0
        h=len(heights)-1
        res=0
        while(l<h):
            curr=(h-l)*min(heights[l], heights[h])
            res=max(curr,res)
            if heights[l]<heights[h]:
                l+=1
            else:
                h-=1
        return res

        