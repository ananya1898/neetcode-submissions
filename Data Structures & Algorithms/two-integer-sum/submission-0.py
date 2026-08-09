class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        difference={}
        for i in range(len(nums)):
            if target-nums[i] in difference.keys():
                return [difference[target-nums[i]],i]
            else:
                difference[nums[i]]=i

        