"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
typically using all the original letters exactly once.

Example:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

"""
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        if len(strs)==0:
            return [[""]]
        empty=[]
        not_empty=[]
        for str_ in strs:
            if str_ =="":
                empty.append(str_)
            else:
                not_empty.append(str_)
        
        letters=["","a","b","c","d","e","f","g","h","i","j","k",
                "l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
        embed=dict()
        anagram=dict()
        result=[]
        ########
        for words in not_empty:
            value=0
            for letter in words:
                value+=letters.index(letter)
            embed[words]=value
        #######
        val=set(embed.values())
        
        for values in val:
            anagram[str(values)]=[element for element in embed.keys() if embed[element]==values]
            
        for keys in anagram.keys():
            result.append(anagram[keys])
        if len(not_empty)!=0 and len(empty)!=0:
            return [empty]+result
        if len(not_empty)==0 and len(empty)!=0:
            return [empty]
        if len(empty)==0 and len(not_empty)!=0:
            return result

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