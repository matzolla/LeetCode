def  ocean_view(arr):
     # heights =[4,2,3,1]
      stack= [] # [3]
      for idx in range(len(arr)):
           while len(stack) and arr[stack[-1] ]< arr[idx]:
                   item = stack.pop()
         
           stack.append(idx)
     return stack 
                   
    
def  ocean_view(arr):
   stack=[]  # heights =[1,3,2,4] ->[3]

      max_val= -float(‘inf’) # [3]  [0,2,3]
      for idx in reversed(range(len(arr))): 3,2,1,0
           If arr[idx]> max_val:
              max_val=arr[idx]
              stack.append(idx)  # [0
     return reversed(stack)
