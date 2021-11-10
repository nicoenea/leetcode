class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(1, len(prices)): # iterate through array
            if prices[i] > prices[i-1]: # if current is greater than prev
                profit = profit  + prices[i] - prices[i-1] # store profit and add current, subtract prev
        return profit
    
    