def meeting_planner(slotsA, slotsB, dur):
  # your code goes here
  # time complexity O(N+M)
  #space O(1)
  
  idx,idy=0,0
  #min_val= float('inf')
  Interval=[]
  while idx<len(slotsA) and idy < len(slotsB):
    
    startx,endx= slotsA[idx]
    starty,endy= slotsB[idy]
    
    
    start= max(startx,starty)
    end= min(endx,endy)
    
    if start+dur <= end: return [start,start+dur]
    
    if endx< endy : idx+=1
      
    else: idy+=1
      
  return Interval
        
