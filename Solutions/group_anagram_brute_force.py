"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
typically using all the original letters exactly once.

Example:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

"""
### really brute-force approach time complexity ~0(n^2)
## space complexity O(len(result)) with some auxillary space complexity

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        
        anagrams=collections.defaultdict(list)
        
        for str_ in strs:
            
            anagrams[tuple(sorted(str_))].append(str_)
            
        return anagrams.values()


## time complexity O(nm.log(n))  i think the sorting has an impact on the algorithm
