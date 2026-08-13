class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums=sorted(nums)
        n=len(nums)
        res=[]
        for i in range(n):
            j=i+1
            k=n-1
            while(j<k):
                if nums[j]+nums[k]==-nums[i]:
                    res.append((nums[i],nums[j],nums[k]))
                    j+=1
                    k-=1
                elif nums[j]+nums[k]>-nums[i]:
                    k-=1
                else:
                    j+=1
        return list(set(res))




        