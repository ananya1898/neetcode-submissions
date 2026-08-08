class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        s1={}
        s2={}
        for i in range(0,len(s)):
            if s[i] not in s1:
                s1[s[i]]=0
            else:
                s1[s[i]]+=1
            if t[i] not in s2:
                s2[t[i]]=0
            else:
                s2[t[i]]+=1              
        if s1==s2:
            return True
        return False

            
        