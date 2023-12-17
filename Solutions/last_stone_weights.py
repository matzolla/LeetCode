import heapq

# heapify the stones
stones = [-1*val for val in stones]
heapq.heapify(stones)

# extract the two max values 👍

while len(stones)>1:

   weight1= heapq.popleft(stones)
   weight2= heapq.popleft(stones)

   # compute difference 
   difference= abs(-1*weight1-(-1*weight2))
   if difference ==0:
         continue
   else:
       heapq.heappush(stones,difference)

return stones[0] if len(stones)==1 else 0
