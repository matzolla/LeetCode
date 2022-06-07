"""You have planned some train traveling one year in advance. The days of the year in which you will travel are given as an integer array days. Each day is an integer from 1 to 365.

Train tickets are sold in three different ways:

a 1-day pass is sold for costs[0] dollars,
a 7-day pass is sold for costs[1] dollars, and
a 30-day pass is sold for costs[2] dollars.
The passes allow that many days of consecutive travel.

For example, if we get a 7-day pass on day 2, then we can travel for 7 days: 2, 3, 4, 5, 6, 7, and 8.
Return the minimum number of dollars you need to travel every day in the given list of days.

"""

class MincostTicket(object):

    def Mincost(self,days,cost):

        # Input days: list of days
        # Cost: list cost ticket
        # Output : cost travel N-days

        days_pass=[1,7,30]

        dp= [0]*(max(days)+1)


        for day in days:

            for j in  range(len(days_pass)):

                if days_pass[j] <= day:

                    dp[day]=min(dp[day], dp[day-days_pass[j]])+ cost[j]
                else:
                    dp[day]=dp[day-1]



        return dp[-1] 




######### Complexity analysis ###########

## space: O(log(len(days)))
## Time : O(mn)  where m is len(days) and n len(cots)

