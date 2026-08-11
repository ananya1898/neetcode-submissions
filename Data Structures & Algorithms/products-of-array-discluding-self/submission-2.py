class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zeroes=0
        totalProduct=1
        for x in nums:
            if x==0:
                zeroes+=1
            else:
                totalProduct*=x
        res=[0]*len(nums)
        
        if zeroes==0:
            for i in range(len(nums)):
                res[i]=int(totalProduct/nums[i])
        elif zeroes==1:
            for i in range(len(nums)):
                if nums[i]==0:
                    res[i]=totalProduct
        return res        

        
        