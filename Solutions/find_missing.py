def find_missing(arr):
  # time O(N)
  # space O(1)
  # using set to 'look up' on the data base
  MAX_INT= 2^31-1
  
  seen = set(arr)
  
  for idx in range(len(arr)):
    
    if idx not in seen: return idx
    
    
  return len(arr) if len(arr)< MAX_INT else MAX_INT
