import math
# Add any extra import statements you may need here


# Add any helper functions you may need here


def numberOfWays(arr, k):
  # Write your code here
  # [1,1,3,6]
  # for loops
  ## time O(N) space O(1)
  sums=[]
  hashset=set()
  cum_sum=0
  for idx in range(len(arr)):
    cum_sum+=idx
    sums.append(cum_sum)
  sums[0]=1 
    
  ## now count numbers
  ##  {1:1,2:1,3:2,4:1}
  hashtable={}
  for num in arr:
    if num not in hashset:
      hashtable[num]=1
      hashset.add(num)
    else:hashtable[num]+=1
      
  ## pair sum
  #{1,2,3}
  result=0
  seen,check=set(),set()
  for num in arr:
    
    if (k-num in seen) and (k-num not in check):
      result+=sums[hashtable[k-num]-1]
      check.add(num)
    seen.add(num)
    
    
  return result
