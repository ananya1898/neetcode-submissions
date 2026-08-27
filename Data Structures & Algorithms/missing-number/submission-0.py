class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        expectedSum=(n*(n+1))//2
        actualSum=sum(nums)
        missingNumber=expectedSum-actualSum

        return int(missingNumber)