class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        
        ## #i have  brute force approach time complexity O(nm)
        intersect=[]
        for idx in range(len(nums1)):
            
            for idy in range(len(nums2)):
                
                if nums1[idx]==nums2[idy]:
                    
                    intersect.append(nums1[idx])
                    
                    nums2[idy]='y'
                    nums1[idx]='x'
                    
        return intersect 
      
      
 ### time complexity O(nm)
