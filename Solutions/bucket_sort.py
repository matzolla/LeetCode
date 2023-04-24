"""
array=[0.43,0.32,0.32,0.21,0.11,0.56]
"""
def bucket_sort(array):
  
  ### initialize buckets:
  
  bucket=[]
  result=[0]*len(array)
  for idx in range(len(array)):
    bucket.append([])
    
  for idx in range(len(array)):
    index= int(idx*10)
    
    bucket[index].append(array[idx])
    
  for idx in range(len(array)):
    bucket[index]=sorted(bucket[index])
    
  ### upto now the time complexity is O(n)
  
  k=0
  for idx in range(len(bucket)):
    for idy in range(len(bucket[idx]):
           array[k]=bucket[idx][idy]
           k+=1
                     
  ### time complexity O(nm)
