class Solution:
    def findMin(self, nums: List[int]) -> int:
        l=0
        h=len(nums)-1
        if nums[l]<=nums[h]:
            return nums[0]
        while(l<h):
            m=(l+h)//2
            if nums[h]<nums[m]:
                l=m+1
            else:
                h=m
        return nums[l]
            
         