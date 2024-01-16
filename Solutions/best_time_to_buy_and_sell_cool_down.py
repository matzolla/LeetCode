class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        we have for actions 
        action1- has 0 stock and buy 1
        action2- has 0 stock do nothing
        action3- has 1 stock sell
        action4- has 1 stock do nothing

        very interesting
        """
        if len(prices)<2: return 0
        
        action_1= -prices[0]
        action_2=0
        action_3= 0
        action_4= -prices[0]

        for idx in range(len(prices)):

            l1=action_1
            l2=action_2
            l3=action_3
            l4=action_4

            action_1= l2-prices[idx]
            action_2= max(action_3,action_2)
            action_3= max(action_1,action_4) +prices[idx]
            action_4= max(action_1,action_4)
        
        return max(action_2,action_3)
