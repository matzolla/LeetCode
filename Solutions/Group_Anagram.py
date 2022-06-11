"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
typically using all the original letters exactly once.

Example: 
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

this can be a better amelioration of brute force but still needs ameliorations but gives a paste on atleast how to 

solve it!!!
"""

class solution(object):

    def Group_anagram(self,strs):

        # Input a list of strings [str]
        # Output a list of lists  of strings[[str]]
        concat_str=''

        encoded_words=[]

        words=[]    #append str in words
        ana=set()   # append the anagram 
        anagram=[]  # append the list of anagrams

        output=[]
        for str in strs:

            concat_str+=str

        unique_char= set(concat_str)     ## here we start by retrieving the uniqque characters Time complexity O(k), with k=len(concat)

        for word in strs:
            ## initializing a dict with default values 0
            encode=dict.fromkeys(list(unique_char),0)
            for str in word:
                encode[str]=1            ### here we encode each word into with respect to the unique characters {}  time complexity O(m*n) where m=len(words), n=len(unique_char)

            encoded_words.append(encode)
            words.append(word)


        for encode in encoded_words:
            for encoded,wrd in zip(encoded_words,words):   ### time complexity O(m^2) where m =len(encoded_words)

                if encode==encoded:
                    ana.add(wrd)
            
            anagram.append(list(ana))

            ana.clear()
        [output.append(x) for x in anagram if x not in output]

        return anagram


        ### Time complexity ########
        ## O(m^2+m*n+k)~ O(m^2)


        ## space complexity #######
        ## many auxillary space complexity---s