class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if len(s2)<len(s1):
            return False

        freqS1={}
        freqS2={}
        for x in s1:
            if x not in freqS1:
                freqS1[x]=1
            else:
                freqS1[x]+=1
        l=0
        r=len(s1)
        for x in s2[l:r]:
            if x not in freqS2:
                freqS2[x]=1
            else:
                freqS2[x]+=1
        
        if freqS1==freqS2:
            return True
        
        for i in range(1,len(s2)-len(s1)+1):
            freqS2[s2[i-1]]-=1
            if freqS2[s2[i-1]]==0:
                freqS2.pop(s2[i-1])
            if s2[i+len(s1)-1] not in freqS2:
                freqS2[s2[i+len(s1)-1]]=1
            else:
                freqS2[s2[i+len(s1)-1]]+=1
            if freqS1==freqS2:
                return True
        return False


               