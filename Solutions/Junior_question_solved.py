[6 7 4] 10
 4 4  4 
[5,3,2] 10
left_over_wood=0

for length in wood:
   If length<= left_over_wood:
       “”” do nothing “”””
   else;
      “”increment””
   left_over_wood=max(left_over_wood, L-length)
### Time complexity O(N)
### space complexity O(1)
