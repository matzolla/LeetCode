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
-  `Container with most water:` I have one brute force approach with a time complexity of O(n^2) (two for loops while computing the area at each step to get the maximum area). Now using the two pointer approach, I put a left pointer and a right pointer and compare the height of both pointers. the areas can be calulated by multiplying the smallest height with the difference between the indices of the vertical lines and make sure to always keep the maximum area.
-  `intersection of two arrays II:` I think it's a brute force approach. A double for loop moving across the two arrays. If nums1[idx]=nums2[idy], then this is an intersect. now replace these numbers with something else (may be characters for my case) , to prevent duplicates. nums1[idx]=`x` and nums2[idy]=`y`. Time complexity O(nm) (with `n`=len(nums1) and `m`=len(nums2))
-  `3closest sum:` I proposed a brute force approach with time complexity `O(n^3)` that i later optimized to `O(n^2)` using sorting and two pointers, but this solution can be optimized better to `O(nlogn)` with binary search (two pointer still) see link: https://leetcode.com/problems/3sum-closest/discuss/1365756/C%2B%2B-Binary-search
-  `longest palindromic substrings`: https://iq.opengenus.org/longest-palindromic-substring-dp/ 
-  `Median of two sorted arrays`: strong intuition gotten from https://leetcode.com/problems/median-of-two-sorted-arrays/discuss/2471/Very-concise-O(log(min(MN)))-iterative-solution-with-detailed-explanation time complexity `O(log(min(n,m)))`









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
- `Combination sum IV:` Almost the same as the `coin change` solutions, with a slight change in that dp[i] += dp[i-coins], with the initial condition that dp[0]=1 (then think about the edge cases as well)




#### Graph and Trees
- `Time to inform all employees`: 
- `Validate Binary search Tree`: using dfs, append the (root, max, min) in the stack and proceed with dfs traversal. If node.val> Max or < Min return false. Otherwise check if left child exist and append (left, min(max,root.val),min) also check for the right child and append (right, max, max(min, node.val)).



#### Linked list

- `merging two linked list`: initialize two linkedlist. while list1 and list2 not `None`,compare the values of each list and assign to one of the initialized linkedlist and traverse the lists. Finally if list1 is not none, the next node of the linkedlust is list1 if list2 is not None, the next node of the linkedlist is list2
- `reverse a linked list`: we initialize a previous node to none then a current node to the head of the list then the next node to curr.next, then curr.next to previous then previous to curr then curr to next (tricky right? :)  )
- `Reorder list`:  We used here the stack data structure to store all the nodes if the node indice in the stack is even, then the head.next is that node, otherwise the head.next is the node at the end of the linkedlist then head=head.next. 


#### Heap DSA and heap sort 

- `Heap sort link to a good tutorial:` https://www.hackerearth.com/practice/data-structures/trees/heapspriority-queues/tutorial/
- `Implemented heapify and max_heap tutorial 1` colab link : https://colab.research.google.com/drive/1t5-1chLNa90tEXip-eXNIaPwY5abmh33?usp=sharing


#### Merge Sort

- `merge sort tutorial:` https://www.programiz.com/dsa/merge-sort `time complexity O(nlogn)`

#### Count Sort

- `Count sort:` https://www.programiz.com/dsa/counting-sort

#### Quick Sort

- `solved`

#### Insertion Sort

#### Bubble Sort

