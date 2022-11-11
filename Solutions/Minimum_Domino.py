class Solution(object):
    def minDominoRotations(self, tops, bottoms):
        """
        :type tops: List[int]
        :type bottoms: List[int]
        :rtype: int
        the test case passed are with a 76/84,
        
        with a small tweak we can get a good pass.
        """
        swap_top=0
        swap_bottom=0
        dict_top=dict.fromkeys(set(tops),0)
        dict_bottom=dict.fromkeys(set(bottoms),0)
        ## dominos at top
        
        flag1=True
        flag2=True
        for num in tops:
            dict_top[num]+=1
        
        ### dominos at the bottom
        for num in bottoms:
            dict_bottom[num]+=1 
        id_top=[idx for idx in range(len(tops)) if tops[idx]!=max(dict_top,key=dict_top.get)]
        id_bottom=[idx for idx in range(len(bottoms)) if bottoms[idx]!=max(dict_bottom,key=dict_bottom.get)]
        for idx in id_top:
            if bottoms[idx]==max(dict_top,key=dict_top.get):
                swap_top+=1
            else:
                flag1=False
        for idy in id_bottom:
            if tops[idy]==max(dict_bottom,key=dict_bottom.get):
                swap_bottom+=1
            else:
                flag2=False
        print(swap_bottom,swap_top)        
        if (flag1 or flag2):
            return min(swap_top,swap_bottom)
        else:
            return -1
