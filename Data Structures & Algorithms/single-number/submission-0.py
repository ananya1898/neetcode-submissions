class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res=nums[0]
        for x in range(1,len(nums)):
            res^=nums[x]
        return res
        