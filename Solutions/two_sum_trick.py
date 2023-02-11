def get_indices_of_item_wights(arr, limit):
  
  ### time o(n)
  ### space o(n)
  hashtable={}
  
  hashset=set()
  
  ### first for loop
  for idx in range(len(arr)):
    
    if arr[idx]  not in hashset:
      hashtable[arr[idx]]=[]
    hashtable[arr[idx]].append(idx)
    
    hashset.add(arr[idx])
  
  
  
  ### second for loop
  seen=set()
  for num in arr:
    
    if limit-num in seen:
      idx=max(hashtable[limit-num])
      idy=max(hashtable[num])
      
      if idx< idy : return [idy,idx]
      elif idx==idy: return [idx,idy-1]
      else: return [idx,idy]
    else:
      seen.add(num)
  return []
      
  
  
  
