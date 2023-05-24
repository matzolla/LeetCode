class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        result=[]
        keyboard=[
                  ['q','w','e','r','t','y','u','i','o','p'],
                  ['a','s','d','f','g','h','j','k','l'],
                  ['z','x','c','v','b','n','m']
                  ]
        
        encode_key= collections.defaultdict()


        for key, row in enumerate(keyboard):

            for letter in row:

                encode_key[letter]=key+1


        for word in words:
            check=1
            for char in word:
                # check.append(char)
                check*= encode_key[char.lower()]
            # check= ''.join(check)
            if (check==1**len(word) or check == 2**len(word)or check==3**len(word)):
                result.append(word)



        return result
