class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        
        [0,1,2,3,4,5,6,7,8]
        
        [1,8,6,2,5,4,8,3,7]
             _ _
        """
        area=0
        ### first step complexity O(n)
        lines=[]
        for index, heights in enumerate(height):
            
            lines.append((index,heights))
            
        
        left=0
        right=len(lines)-1
        
        while left<right:
            
            id_left, h_left=lines[left]
            id_right, h_right=lines[right]
            
            if h_left>h_right:
                
                area= max(area, h_right*(id_right-id_left))
                right-=1
                
            elif h_right>h_left:
                area= max(area,h_left*(id_right-id_left))
                left+=1
            else:
                area= max(area,h_left*(id_right-id_left))
                left+=1
                right-=1
        
        return area
        
        
        ## Time complexity O(n)
