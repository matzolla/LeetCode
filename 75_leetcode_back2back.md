## Currated list 75 leetcode questions to save your time 

##### Arrays 
- `Two sums` : If nums-a in set, then return the solution [a,b] else add (a) in the set.
-  `Best time to buy and sell stocks`: initialize a profit as the difference btwn the selling price and buying price then update by computing the maximum profit, make sure to always minimize the buying prize by updating it as well.
-  `Contains duplicates`: can just use a set if the len of the set is less than the initial list then it contains a duplicate.
-  `Product of array except itself`: perform prefix product on the array, then perform suffix product on the array again, at the end multiply both results
-  `maximun subarray`: start by initializing a curr_sum variable to zero and largest sum to -inf save the maximum value between the curr_sum + number and number itself if the curr_sum is greater than the largest sum, then the largest_sum= curr_sum.
-  `maximum product sub-array`: create two variables minA and maxA, then compute the maxA=max(maxA*sum, curr, minA*sum) and the minA=min(minA*sum,curr,maxA), and keep iterating until we get the maximum product array.
-  `minimium value in rotated sorted array:` Initialize a left pointer at 0 and a right pointer at n-1 and a middle pointer. While the left is less than the right, if the number at the middle is less than the number at the right, then the left=middle. else left=middle+1.
-  `search in rotated sorted array:` Binary search as usual. Initialize a left and right pointer, compute the middle pointer, if left<middle, check if left<target<middle, the decrement the right pointer (right=middle-1) if yes or increment the left pointer(middle+1) if no. Do same on the other way round (for left>middle).
-  `Container with most water:` I have one brute force approach with a time complexity of O(n^2) (two for loops while computing the area at each step to get the maximum area). Now using the two pointer approach, I put a left pointer and a right pointer and compare the height of both pointers. the areas can be calulated by multiplying the smallest height with the difference between the indices of the vertical lines and make sure to always keep the maximum area.
-  `intersection of two arrays II:` I think it's a brute force approach. A double for loop moving across the two arrays. If nums1[idx]=nums2[idy], then this is an intersect. now replace these numbers with something else (may be characters for my case) , to prevent duplicates. nums1[idx]=`x` and nums2[idy]=`y`. Time complexity O(nm) (with `n`=len(nums1) and `m`=len(nums2))
-  `3closest sum:` I proposed a brute force approach with time complexity `O(n^3)` that i later optimized to `O(n^2)` using sorting and two pointers, but this solution can be optimized better to `O(nlogn)` with binary search (two pointer still) see link: https://leetcode.com/problems/3sum-closest/discuss/1365756/C%2B%2B-Binary-search. Better update https://leetcode.com/problems/3sum-closest/discuss/2675440/Python-Easy-O(N2)-Solution-with-removed-iteration-for-same-set-of-3-values.
-  `longest palindromic substrings`: https://iq.opengenus.org/longest-palindromic-substring-dp/ 
-  `Median of two sorted arrays`: strong intuition gotten from https://leetcode.com/problems/median-of-two-sorted-arrays/discuss/2471/Very-concise-O(log(min(MN)))-iterative-solution-with-detailed-explanation time complexity `O(log(min(n,m)))`
-  `Find first and last position`: It's obviously done using binary search. But in this case we need to define a function for the last element and first element respectively. For the first element, if the mid==target, then the first element= mid. but now we need to say the righ=mid-1 and keep the iteration to return the start. For the last element, if the mid==target then the last element=mid and low=mid+1, (so as to check if the rightmous element is also the target).
-  `Insert interval`: The intervals are already sorted so one need to check if the incoming interval does not overlap with the other intervals. Two conditions if newInterval[0]> interval[idx][1] or newInterval[1]< interval[idx][0] then the intervals doesn't overlap. Otherwise, the newInterval=[min(interval1,interval2),max(interval1,interval2)].
-  `Merge Intervals`: We start by sorting the intervals by first array. We create a list in which we append the first element of the array of intervals. When `for looping` the remaining array, if the start is less than the last element in the previous sequence...then merge the arrays otherwise just append the arrays. (`time complexity of O(nlogn)`)
-  `continuous subarray sum:` For now the run time is O(n^2) with a space complexity of O(1).
-  `contiguous array:` a double for loop while counting the number of zeros and 1 and -1. Don't forget to change the value `0` to `-1` then start a dictionary at index `-1` with value `0`.If they are equal, then consider the length of the subarray.The runtime will be O(n^2). It can be further optimized using a hashmap where we store the index of a sum as we go throught the loop and (while keeping the incrementation) and if we encounter that sum again then we take into consideration the difference between the index of that sum and the actual index where we are. Have a look [here](https://leetcode.com/problems/contiguous-array/solutions/1743341/c-simplest-solution-optimization-from-brute-force-one-pass/?orderBy=most_relevant)
-  `find kth positive missing value:` we traverse the array an check if the arr[idx]-(idx+1) is greater than `k`. If this is the case, then we return `idx+k`, otherwise we return len(arr)+k and that's it. But theres a better way to improve this model using binary search for a time complexity `O(logn)`
-  `Array partition:`
-  `don't forget the array.index(function)`: to be noted
-  `Solved search insert position`: With `O(logn)` time complexity and `O(1)` space.
-  `Boats to save people`: We start by sorting the array. Then we use the two pointer approach to check whether the sum of two people's weight are less than or equal to the limit weights, if that's the case then we increment the left pointer and decrement the right pointer, we also count the number of boats as `1`. Otherwise we just decrement the right pointer and make sure that the number of boats is also incremented by `1`.
-  `New transaction (very interesting)`: [here](https://leetcode.com/problems/invalid-transactions/submissions/932554280/)
-  `Sign of product`: We loop through the value of the array and we keep multiplying the variable `product` at the end we check the sign.
-  `Target sum`: An idea is better than nothing, link [here](https://leetcode.com/problems/target-sum/) using backtracking to resolve it. It obviously will have an exponential time comlexity $O\left(n^\alpha\right)$
-  `Difference of two arrays`: Simply by using sets and the `difference` property of set can help identify elements who are not in the set or who actually are.
- `Diagonal sum`: Just a normal sum while considering the fact that the middle index in the matrix shouldn't be crossover twice.






#### Stack and Queues:
- `Implementing a queue using stack:` This is also very interesting link [here](https://leetcode.com/problems/implement-queue-using-stacks/solutions/127533/implement-queue-using-stacks/?orderBy=most_relevant)
- `Valid parenthesis:` Simply append the element in the stack and pop it to verify if it's a valid parenthese.



#### Dynamic Programming:

- `Longest Increasing subsequence`: double for loop, check if nums[i]>nums[j] for i in range(len(nums)), and for  j in range(0,i), dp[i]=max(dp[i],dp[j]). Using the double for loop, else we move out of the first loop and increment dp[i]+=1. Then we can return the `max(dp)`.
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
- `maximum envelopes`: A variant of longest increasing subsequence, with some conditions.
- `Best time to buy and sell with cooldown` very interesting explanation [here](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/solutions/75930/very-easy-to-understand-one-pass-o-n-solution-with-no-extra-space/?orderBy=most_relevant).

#### Matrices
-`Multiplying two matrices:` So far I used the normal equation with a run time complexity of O(n^3) but there's a better approach using divide and conquer algorithm.
- `Spiral matrix:` Revision
- `Set matrix to zeros`: The idea is to store the indice of all the row and all the column to be set to zero then using a second for loop perform the zeroing on each of this indexed zero value. Time complexity `O(mn)`




#### Graph and Trees
- `Time to inform all employees`: 
- `Validate Binary search Tree`: using dfs, append the (root, max, min) in the stack and proceed with dfs traversal. If node.val> Max or < Min return false. Otherwise check if left child exist and append (left, min(max,root.val),min) also check for the right child and append (right, max, max(min, node.val)).
- `Binary Tree Coloring Game`: I will always play inorder to have the maximum number of counts. I have 3 options, counting the left child, the right child and the parent. The best move will be if one count is greater than the sum of the two others.
- `Number of Island`: Solved using dfs or bfs
- `Maximum/ Minimum number of Island`:
- `Binary Tree Inorder and Preorder traversal`: for inorder traversal, traverse the left part of the tree then the right before moving to the root. Small notice `preorder trasversal is like a simple dfs`
- `Lowest common ancestors`: A really tough one, the idea is to do a bfs traversal, while storing the nodes in each level as well as the parents of each ancestor in a dictionary. If the lowest common ancestors is in the level dictionary whose height is the highest. If the number of nodes in this level is one, then just return it. otherwise we look for the parents of each node in the deepest level, and check whether the we fall on a common ancestor node (a node which is common to each node)
-  `Same tree:` We start at each node if the node p and q doesn't exist we return True, if one of the node exist we return False if the values of the two nodes are different return False. Perform a recursion on both the pair of left nodes and pair of right nodes.
-  Revised some concepts on graphs, (`connected components`,`find_path`,`longest_path`,`max size of component`,`adjacency matrix`,`dfs and bfs trasversal`).
-  `Solve the leetcode 1519:` (atleast bruteforce solution to understand the concept)
-  `maximum width of a binary tree:` check out this link [here](https://leetcode.com/problems/maximum-width-of-binary-tree/solutions/726732/Python-10-lines-BFS-explained-with-figure/)
-  `Minimum spanning trees (MST):` [Here](https://leetcode.com/problems/min-cost-to-connect-all-points/solutions/843930/accepted-python-3-minimum-spanning-tree-kruskal-s-algorithm-union-find/?orderBy=most_relevant)

#### Strings 
- Don't forget this syntax on strings `.lower()`,`.upper()`,`.isupper()`,`.islower()`, `.isspace()`
- In a dictionary dic to get the value of a key, we can say `.get(dic[key],0)`.
- `longest repeating char replacement:` We initialize a left index `0` and right index `0` next we use a for loop to increment the right index and count the number of occurence of the character in a dictionary. We also define a condition if a window is valid meaning `right-left+1 - max(count)>k` we decrement the count of the left character and increament the left index. then we return the max window size.
- `lowes lexical string from root:` We start by creating a stack (using dfs) the stack contains (node, string) we traverse the tree while adding the each character down the node....until we get to the leaf (a node is consider a leaf if the left and right child doesn't exist). For this particular nodes we collect the string obtained. then we look for the lexicographically smallest string (for now we use the sorting algorithm). 
- `Optimal partition of string:` We define an empty set where we keep adding characters. Once we detect a repeating character, we reset the set and increment a count variable by one.

#### Linked list

- `merging two linked list`: initialize two linkedlist. while list1 and list2 not `None`,compare the values of each list and assign to one of the initialized linkedlist and traverse the lists. Finally if list1 is not none, the next node of the linkedlust is list1 if list2 is not None, the next node of the linkedlist is list2
- `reverse a linked list`: we initialize a previous node to none then a current node to the head of the list then the next node to curr.next, then curr.next to previous then previous to curr then curr to next (tricky right? :)  )
- `Reorder list`:  We used here the stack data structure to store all the nodes if the node indice in the stack is even, then the head.next is that node, otherwise the head.next is the node at the end of the linkedlist then head=head.next.
- `odd even linkedlist`: The intuition is to create an even part and an odd part of the linked list let say even =head.next,also evenHead=head.next and odd=head then while even and even.next, the odd.next= even.next (then odd=odd.next) also the even.next= odd.next and even=even.next. now the odd.next=evenHead we can now return the head.
- `finding the middle of linkedlist:` For that we need a fast and slow pointer where while fast and fast.next we update slow to slow.next and fast to fast.next.next at the end return slow.
- `Rotating list:` we start by getting the number of rotations by performing a modulus over the length of the nodes (n) and the number of shift k. if n=1 or k<=0 or no nodes are found then return the head. We run the node into its n-k distant apart. then split the node into two parts at that point (split the nodes into two). Run the second split until its to the end node such that the next node to it is the first split. Then return the second split as output.
- `swaping nodes in pairs:` Have two methods, we can replace the value of each node in place (easiest way). Or we can swap the nodes literally! we start by defining an empty dummylist which point to the head of the linked list (ll). We define a node `prevnode` equal to the dummy ll and a current node `currnode` equal to the head of the ll. The `prevnode.next` will be pointing toward the next node of currnode `currnode.next` and the `currnode.next` pointing at `prevnode.next.next`. The variable `prevnode.next.next` points to the `currnode` and the `prevnode=currnode` at this level the `currnode=currnode.next`.
- `adding two linked list:` Almost the same as adding two numbers in a list (but in this case we use two linked list. Take care of the remainder when using the modulus operation.)
- `merging k linked list:` Using an approach similar to `devide and conquer` that renders me a time complexity of `O(nlogk)`.

#### Bit manipulation
- `pow(x,n)`: a normal for loop with a linear time will not be efficient especially if you do multiply let say 1 a thousand time. hence we used bit manipulation to obtain an exponential time complexity O(logn)
- `count ones`: count the number of ones (something like that :))
- `reverse bit:`


#### Heap DSA and heap sort 

- `Heap sort link to a good tutorial:` https://www.hackerearth.com/practice/data-structures/trees/heapspriority-queues/tutorial/
- `Implemented heapify and max_heap tutorial 1` colab link : https://colab.research.google.com/drive/1t5-1chLNa90tEXip-eXNIaPwY5abmh33?usp=sharing 
- Implemented a better version of the heap data structure
- `Top K frequent element:` Start by counting the number of occurence of each element in the array. Then use a priority queue to pop the topK element with respect to the frequency of occurence.
- `Single threaded CPU:` interesting thought [here](https://leetcode.com/problems/single-threaded-cpu/solutions/2216661/single-threaded-cpu/?orderBy=most_relevant)
- `median of a data stream:`


#### Merge Sort

- `merge sort tutorial:` https://www.programiz.com/dsa/merge-sort `time complexity O(nlogn)`

#### Count Sort

- `Count sort:` https://www.programiz.com/dsa/counting-sort

#### Quick Sort

- `Quick sort:` [coming soon](https://github.com/matzolla/LeetCode/blob/main/Solutions/quick_sort.py)


#### Insertion Sort

- `solved:` https://github.com/matzolla/LeetCode/blob/main/Solutions/tri_par_inserition.py

#### Bubble Sort

- `Bubble sort:` https://www.programiz.com/dsa/bubble-sort


#### Back-tracking Algorithm

- `Combination sum`: check out the link [here](https://github.com/matzolla/LeetCode/blob/main/Solutions/combination_sum_backtrack.py)
- `Also did generate parenthesis`:
- `permutation:` using a simple back-tracking algorithm

#### Trie data structure

- `Tutorial on Trie` very interesting tutorial [here](https://www.geeksforgeeks.org/introduction-to-trie-data-structure-and-algorithm-tutorials/)

#### Dealing with monotonic Stack

- `Interesting pratical examples:` link [here](https://itnext.io/monotonic-stack-identify-pattern-3da2d491a61e)

## Google Online Assessment

- `Minimum Difference Between Largest and Smallest Value in Three Moves`: Sort the array, remove the last three element,  compute the amplitude, remove the last element and the first 2 , remove the last 2 and the first element, remove the first 3 element.
- `Way to split string`: We can do a dynamic slidding window, and seperate the string into two strings and always check if the number of unique characters in `string1` and `string2 ` are equal.
- `Maximum Time`: Not really efficient but we can always check the different conditions where the time doesn't exist example ??:59==23:59 and so on.
-  `Most booked hotel room`: in a dictionary we count out the hotels which are booked and get the maximum values using `max(dict.values)` if we have dict as dictionary, then we can have key, values from dict.items() [key for key,value in dict.items if value==max(dict.value)].
-  `Minimum Domino tweak`: link [here](https://github.com/matzolla/LeetCode/blob/main/Solutions/Minimum_Domino.py)
-  `time to typestring`: we start by creating a dictionary, with keys the letters and the values the index, next to it we initialize a list, of len the size of the text, then we initialize the first value as the index of the first character to type. We can therefore compute the other using a 1d dynamic programming task like this dp[idy]= abs(dp[idy-1]- dico[txt[idy]]) then at the end we can sum sum(dp).
-  `very important tip on dynamic programming:` link [here](https://leetcode.com/problems/palindromic-substrings/discuss/2062005/Python-Simple-Python-Solution-Using-Two-Different-Approach).
-  `Online assesment cleared from singapore`: Solution in my brain :) link to questions [here](https://github.com/desmondyeoh/Google-Online-Challenge-solutions)
## Interview Prep Hub Meta
- Link [here](https://www.metacareers.com/profile/interview_prep_hub)
- Further info coming soon.
## Next STEP
- `Simulating Interview:` Building my solution for Google Interviews [here](https://docs.google.com/document/d/1EGoCCqTVGySa6FEDUhF09MVcyh_jkC7IJFG0x5TpnR8/edit?usp=sharing)
- `maximum envelope`: Time complexity of O(n^2 + nlog(n)) can be improved to O(nlog(n)) if we use Longest increasing Subsequence on the height only

## COURSES ON LLMS
- https://www.kaggle.com/code/aliabdin1/llm-01-how-to-use-llms-with-hugging-face
- https://stanford-cs324.github.io/winter2022/lectures/introduction/
- https://ankiweb.net/about
## keep the consistency!!
