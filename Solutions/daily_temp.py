class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        let's use monotonic stacks
        time complexity O(N)
        space complexity O(N)
        """

        stack=[]
        result=[0]*len(temperatures)

        for idx in range(len(temperatures)):

            while len(stack) and temperatures[stack[-1]]<temperatures[idx]:
                item=stack.pop()

                result[item]=idx-item

            stack.append(idx)
        
        return result
