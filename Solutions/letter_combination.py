class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        
        """
        self.digits=digits
        dic={"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
        letters=[]
        curr_dig=[]
        ans=[]
        for string in self.digits:
            letters.append(dic[string])  ## [“abc”, “def”]
        
        def back_track(letters_comb,curr_digit,result,Index):
            
            if Index>len(letters_comb)-1: return
            
            if len(curr_digit)==len(letters_comb):
                result.append(list(curr_digit))
                return 
            for  letter in letters_comb[Index]:
                curr_digit.append(letter)
                print(curr_digit)
                back_track(letters_comb,curr_digit,result, Index+1)
                curr_digit.pop()
        
        
        back_track(letters,curr_dig,ans,0)
        
        
        return ans
