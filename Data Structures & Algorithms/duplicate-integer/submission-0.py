class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        set1=set()
        for number in nums:
            if number in set1:
                return True
            set1.add(number)
        return False
        