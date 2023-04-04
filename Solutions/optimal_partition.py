class Solution(object):
    def partitionString(self, s):
        """
        :type s: str
        :rtype: int
        abacaba
        time complexity O(N)
        space complexity O(len(s))
        """

        seen=set()
        count=0
        for char in s:
            if char in seen:
                count+=1
                seen=set()
            seen.add(char)

        return count+1
