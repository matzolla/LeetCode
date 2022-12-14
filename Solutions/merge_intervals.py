class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        ## time complexity O(nlogn)
        ## space complexity O(m) with m=len(results)
        ## we sort 

        intervals.sort(key= lambda i: i[0])
        result=[intervals[0]]

        for start,end in intervals[1:]:

            lastend=result[-1][1]

            if start<= lastend:

                result[-1][1]=max(end,lastend)
            else:
                result.append([start,end])

        return result



    
