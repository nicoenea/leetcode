class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Essentially what we want to do is get the profit onn any given i-th and save it, 
            until we reach the end of our list
        """
        # keep the minPurchase, in case the stock bought on i-th day is minimum and sold later
        minPurchase = prices[0]
        # keep track of maximum Profit
        profit = 0
        for i in prices: # iterate through prices
            profit = max(profit, i - minPurchase) 
            minPurchase = min(minPurchase, i) 
        return profit
        
