"""
Question:
You are assigned to put some amount of boxes onto one truck. You are given a 2D array boxTypes, where boxTypes[i] = [numberOfBoxesi, numberOfUnitsPerBoxi]:

numberOfBoxesi is the number of boxes of type i.
numberOfUnitsPerBoxi is the number of units in each box of the type i.
You are also given an integer truckSize, which is the maximum number of boxes that can be put on the truck. 
You can choose any boxes to put on the truck as long as the number of boxes does not exceed truckSize.

Return the maximum total number of units that can be put on the truck.
"""
class Solution(object):
    def maximumUnits(self, boxTypes, truckSize):
        """
        :type boxTypes: List[List[int]]
        :type truckSize: int
        :rtype: int
        """
        units=[]
        num_boxes={}  ## hash set
        max_units=0
        look_up=set()   ## lookup O(1)
        for types in boxTypes:
            
            ### 
            unit,num_box=types[1],types[0]
            if unit in look_up:
                num_boxes[str(unit)]+=num_box
            else:
                units.append(unit)
                look_up.add(unit)
                num_boxes[str(unit)]=num_box
            
        ### sort the units Time complexity O(nlogn)
        units.sort(reverse=True)
        
        for unit in units:
            
            if num_boxes[str(unit)]>truckSize:
                
                max_units+=unit*truckSize
                truckSize=0
            else:
                max_units+=unit*num_boxes[str(unit)]
                truckSize-=num_boxes[str(unit)]
                
        return max_units
                
            
        #Time complexity O(nlogn+n)~O(nlogn)
        # Space complexity O(m) with m=len(units)
