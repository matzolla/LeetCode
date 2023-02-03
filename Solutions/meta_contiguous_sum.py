# Add any extra import statements you may need here

# [3, 4, 1, 6, 2]
# Add any helper functions you may need here
# runtime o(n^2), space o(n)
def left_contiguous(arr,index):
  
  idx=index-1
  count=0
  flag=True
  while idx>-1 and flag:
    
    if arr[idx]<=arr[index]:
      idx-=1
      count+=1
      
    else: 
      flag=False
      
  return count

def right_contiguous(arr,index):
  
  idx=index+1
  count=0
  flag=True
  while idx<len(arr) and flag:
    
    if arr[idx]<=arr[index]:
      idx+=1
      count+=1
      
    else: 
      flag=False
      
  return count

def count_subarrays(arr):
  # Write your code here
  
  result=[1]*len(arr)
  
  for idx in range(len(arr)):
    sum_left_right=left_contiguous(arr,idx) + right_contiguous(arr,idx)
    result[idx]+= sum_left_right
    
    
  return result
