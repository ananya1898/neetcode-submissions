class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        diff=[]
        res=[]
        for i in range(len(temperatures)-1,-1,-1):
            while(diff and temperatures[i]>=temperatures[diff[-1]]):
                diff.pop()
            diff.append(i)
            if len(diff)==1:
                res.append(0)
            else:
                res.append(diff[-2]-diff[-1])
        return res[::-1]


