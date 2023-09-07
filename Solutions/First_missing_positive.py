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
