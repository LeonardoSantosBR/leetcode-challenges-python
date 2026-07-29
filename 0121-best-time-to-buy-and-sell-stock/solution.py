class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0] 
        max_profit = 0
        
        for price in prices[1:]:
            max_profit = max(max_profit, price - min_price)
            min_price = min(min_price, price)    
        return max_profit
        
solution = Solution();
solution.maxProfit([7,1,5,3,6,4]);