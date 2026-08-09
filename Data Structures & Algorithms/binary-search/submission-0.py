class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low=0
        high=len(nums)-1
        while(low<=high):
            m=(low+high)//2
            if nums[m]==target:
                return m
            elif target>nums[m]:
                low=m+1
            else:
                high=m-1
        return -1
        