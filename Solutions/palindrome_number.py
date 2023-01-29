class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool

        x=121

        without converting to string

        let's try to do without string
        the idea is to reverse the last half of the number
        and check if the first half and the reverted last half are equal

        time complexity O(N)
        space complexity O(1)
        reverted=0

        while x> reverted:

            reverted= reverted*10 + x%10
            x//=10 (and that's it)

        return x == reverted || x == reverted//10

        """
        ## time complexity O(n)
        ## space complexity O(n) (it varies)

        str_x=str(x)

        left=0
        right=len(str_x)-1

        while left<right:

            if str_x[left]==str_x[right]:
                left+=1
                right-=1
            else: return False
        return True
