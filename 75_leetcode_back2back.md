## Currated list 75 leetcode questions to save your time 

##### Arrays 
- `Two sums` : If nums-a in set, then return the solution [a,b] else add (a) in the set.
-  `Best time to buy and sell stocks`: initialize a profit as the difference btwn the selling price and buying price then update by computing the maximum profit, make sure to always minimize the buying prize by updating it as well.
-  `Contains duplicates`: can just use a set if the len of the set is less than the initial list then it contains a duplicate.
-  `Product of array except itself`: perform prefix product on the array, then perform suffix product on the array again, at the end multiply both results
-  `maximun subarray`: start by initializing a curr_sum variable to zero and largest sum to -inf save the maximum value between the curr_sum + number and number itself if the curr_sum is greater than the largest sum, then the largest_sum= curr_sum.
-  `maximum product sub-array`: 
-  `minimium value in rotated sorted array:` Initialize a left pointer at 0 and a right pointer at n-1 and a middle pointer. While the left is less than the right, if the number at the middle is less than the number at the right, then the left=middle. else left=middle+1.
-  `search in rotated sorted array:` Binary search as usual. Initialize a left and right pointer, compute the middle pointer, if left<middle, check if left<target<middle, the decrement the right pointer (right=middle-1) if yes or increment the left pointer(middle+1) if no. Do same on the other way round (for left>middle).









#### Dynamic Programming:

- `Longest Increasing subsequence`: double for loop, check if nums[i]>nums[j] for i in range(len(nums)), and for  j in range(0,i), dp[i]=max(dp[i],dp[j]+1).
- `robber house`: making decision if we rob the house we make sure not to rob the next house here is an intuition

| reward   | robb=yes     | robb=No|
| ------------- | ------------- | -------- 
| `2`       | `2`       | `0`  | 
| `1`         | `1`      | `2`   |
|  `1`       |   `3`        | `2`       |
|  `2`       |    `4`       |  `2`      |

- `Unique path`: the magic trick dp[i][j]=dp[i-1][j] + dp[i][j-1]
- `decode ways`: first check for leading `0` and check if this conditions are verify 0<nums<=26 if the conditions are satisfied then dp[i]=1. Also check for 2-length strings and verify if it doesn't contains `0` (cause if it contains `0`) then we have considered it in the initial condition, also check if the `2-length` of the string satisfies the condition `0<nums<=26` and that `no leading zero`.
- `Climbing stairs:` Fibonnaci series using the formular f[0]=0 and f[1]=1 and f[i]=f[i-1]+f[i-2] for i starting at 2, return the last element of the array f
- `coin changes:` We start by initializing an array with infinity elements inside taking into consideration that the first element of the array has a 0. for all the elements in the array if the coins<= index, then dp[i]=min(dp[i],dp[coins-i]+1)
- `Combination sum IV:`
