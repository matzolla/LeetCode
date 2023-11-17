def Search(arr_2d,value):
  
  ## time complexity O(logn + logm)
  ## time O(1)
  ## example:

    Row=len(arr_2d)
    Col= len(arr_2d[0])

    top,bot=0,Row-1

    while top<=bot:

        mid= (top+bot)//2

        if value>arr_2d[mid][-1]: 

            top= mid+1

        elif value < arr_2d[mid][0]:
            bot= mid-1

        else:
            break

    if top > bot : return False

    row= (bot+top)//2

    left,right=0,Col-1

    while left <= right:

        mid=(left+right)//2

        if value> arr_2d[row][mid]:

            left=mid+1
        elif value < arr_2d[row][mid]:

            right= mid-1

        else: return True
