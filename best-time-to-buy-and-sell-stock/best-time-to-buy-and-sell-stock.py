class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        
        # We need to know that the maxProfit if selling on any i-th day.
        maxProfit = 0
        # There might also be a scenario where stock bought on i-th day is                  minimum and we sell on another day
        minPurchase = prices[0]
        for i in range(1, len(prices)):	#iterate through list index
            print(i)
            maxProfit = max(maxProfit, prices[i] - minPurchase)
            minPurchase = min(minPurchase, prices[i])
        return maxProfit
        