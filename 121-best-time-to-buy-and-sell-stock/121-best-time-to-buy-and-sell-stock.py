class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPurchase = prices[0]
        profit = 0
        
        for price in prices:
            profit = max(profit, price - minPurchase)
            minPurchase = min(minPurchase, price)
            
        return profit