class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        res=0;curr=0;l=0
        letters=set()
        for r in range(len(s)):
            while s[r] in letters:
                letters.remove(s[l])
                l+=1
            letters.add(s[r])
            curr=(r-l+1)
            res=max(curr,res)
        return res

  
                

        