class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        
        s=catsandog
        wordDict=["cats","dog","sand","and","cat"]
        
        still rough in my head but this is a good pseudo code
        
        """
        result=[False]*(len(s)+1)
        
        for idx in range(len(s)):
            
            for word in wordDict:
                
                window=len(word)
                if idx+window> len(s): continue
                    
                else:
                    if s[idx:window+idx]==word:
                        result[window+idx]=True
                
                
        return result[len(s)]
 ## time complexity O(n*m), space complexity len(result)   
                    
