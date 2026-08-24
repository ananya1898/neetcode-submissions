class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s=set()
        for num in nums:
            s.add(num)
        
        res=0

        for num in nums:
            if (num-1) not in s:
                c=0
                curr=num
                while curr in s:
                    c+=1
                    curr+=1
                res=max(res,c)
            
        return res