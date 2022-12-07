class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        time O(N), space O(1)
        """

        roman_integer={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000,
                  "IX":9,"IV":4,"XL":40,"XC":90,"CD":400,"CM":900}
        hashset=set(roman_integer.keys())
        
        fast=0
        integer=0
        idx=0
        while idx<len(s):

            if s[fast:fast+2] in hashset:
                integer+=roman_integer[s[fast:fast+2]]
                fast+=2
            else:
                integer+=roman_integer[s[fast:fast+1]]
                fast+=1
            idx=fast

        return integer
