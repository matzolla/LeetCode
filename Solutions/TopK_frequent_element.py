class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        using heap algorithm
        """

        dictionary={}
        count=0
        result=[]
        for key in nums:

            if key not in dictionary:
                dictionary[key]=1
            else:
                dictionary[key]+=1

        pairs=[(-1*value,key) for (key,value) in dictionary.items()]

        #defining a heap
        
        heapq.heapify(pairs)

        while count < k:
            value,key= heapq.heappop(pairs)
            result.append(key)
            count+=1
        return result
