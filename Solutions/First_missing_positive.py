"""
Given an unsorted integer array nums, return the smallest missing positive integer.

You must implement an algorithm that runs in O(n) time and uses constant extra space.
"""

### I simply used sets if necessary and check thw difference betweewn two sets.
### If there's no difference, then the next positve value is the max value +1


class solution(object):

    def first_missing_positive(self, array):

        # Input array (un sorted)
        # Output first missing positive value

        max_val= max(array)

        full_array= [i for i in range(max_val+1)]   ### initialize an array that appends values from 0 to max(array)

        array_set=set(array).add(0)       ## adding zero in case it does'nt have the min val should be non-zero and positive

        full_set=set(full_array)


        diff_set= full_set.difference(array_set)  ## select all element that are in full_set, that are not in array set


        if len(diff_set)==0: output= max_val+1

        elif len(diff_set)==1: output= diff_set[0]

        else: output=min(diff_set)


        return output



        ### Example [1,2,-1,4,5,6]

        ## max_val=6

        ## full_array=[0,1,2,3,4,5,6]
        ## set(Example).add(0)={-1,0,1,2,4,5,6}
        ## full_set={0,1,2,3,4,5,6}

        ##diff_set={3}----> missing positive=3

        ## Complexity analysis ####
        ## Time complexity :  O(n) with n= len(full_set)
        ## Space complexity : O(1) with an auxilary space of O(len(full_set))

        