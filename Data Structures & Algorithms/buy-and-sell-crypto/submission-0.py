class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_price=prices[0]
        max_profit=0
        for i in range(1,len(prices)):
            if prices[i]>buy_price:
                curr_profit=prices[i]-buy_price
                max_profit=max(curr_profit,max_profit)
            if prices[i]<buy_price:
                buy_price=prices[i]
        return max_profit

        
        