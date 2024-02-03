import heapq

def sort_k_messed_array(arr, k):  
  # during prep for interview
  sub_array= arr[:k+1]
  heapq.heapify(sub_array)  

  for idx in range(k+1,len(arr)):        
        curr_val= heapq.heappop(sub_array)
        arr[idx-(k+1)]=curr_val
        heapq.heappush(sub_array,arr[idx])

  idy=len(arr)-k-1
  while idy< len(arr):
      curr_val= heapq.heappop(sub_array)
      arr[idy]=curr_val

      idy+=1

  return arr
