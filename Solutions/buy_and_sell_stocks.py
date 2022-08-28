class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        buy_price=prices[0]
        if len(prices)==1:
            return 0
        sell_price=prices[1]
        
        profit= sell_price-buy_price
        
        for i in range(1,len(prices)):
            
            if buy_price> prices[i]: buy_price=prices[i]
                
            profit=max(profit,prices[i]-buy_price)
            
        return profit
      
   ### time complexity O(n) , space complexity O(1).
