"""You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin."""

## This is a variant of the Knapsack problem (implemented later)

#  link understanding Knapstack : https://medium.com/@fabianterh/how-to-solve-the-knapsack-problem-with-dynamic-programming-eb88c706d3cf



class Solution:

    def coin_changes(self,coins,amount):

        # take as input coins in list
        # and amount 
        # Output : int representing the mininum number of coins which sum up to amount

        #Brute Force approach (recursive backtrack algorithm)

        capacities=[float("inf") for i in range(amount+1)] ## initialize a capacity list that contains different Knapstack with varying capacities

        capacities[0]=0

        for coin in coins:

            for id in range(amount+1):

                if coin <= id:     

                    #if the coint value is less than the bag capacity, we have two posibilites
                    # either we keep the current capacity or we keep the remainder that makes up the capacity (id-coin)
                    # By minimizing it, (in Knapstack problem we instead maximize and we use 2 dimensional arrays most often)

                    remainder= id-coin   ## the left over capacity of the bag

                    capacities[id]=min(capacities[id],1+capacities[remainder])


        return capacities[amount] if capacities[amount]!=float("inf") else -1



### complexity analysis

## time complexity O(len(coins)xamount)
## space complexity O(amount)
