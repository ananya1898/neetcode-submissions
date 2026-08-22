class Solution:

    # def climbStairsRec(self,n,dp):
    #     if n==0 or n==1:
    #         return 1
        
    #     if dp[n]!=-1:
    #         return dp[n]
        
    #     dp[n]= self.climbStairsRec(n-1,dp) + self.climbStairsRec(n-2,dp)

    #     return dp[n]
    
    def climbStairs(self, n: int) -> int:
        prev1=1
        prev2=1
        for i in range(2,n+1):
            curr=prev1+prev2
            prev1=prev2
            prev2=curr

        return prev2


    



        