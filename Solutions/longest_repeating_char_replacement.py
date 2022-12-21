class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        Time complexity O(N)
        space complexity O(1)
        """
        longest=0
        counts={}
        left=0

        for right in range(len(s)):
            counts[s[right]]=1+ counts.get(s[right],0)

            while (right-left+1 - max(counts.values()))>k:
                counts[s[left]]-=1
                left+=1
            longest=max(longest,right-left+1)

        return longest
