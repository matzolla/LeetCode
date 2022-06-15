"""
You are given a string s consisting only of the characters '0' and '1'. In one operation, you can change any '0' to '1' or vice versa.

The string is called alternating if no two adjacent characters are equal. For example, the string "010" is alternating, while the string "0100" is not.

Return the minimum number of operations needed to make s alternating.
"""

### Example: "0010" minimum of operations needed is 1 to get:  


class solution(object):

    def minoperate(self,string):
        # Input string
        # output int 

        # start by creating a hashtabke
        
        iterate={"0":"1","1":"0"}
        list_char1=[]   ### for either 0101
        list_char2=[]   ## for either 1010

        ## splitting the string to a list

        list_char1[:0]=string   ### maintain as it is
        list_char2[:0]=string   ### change the first value to its contrary

        list_char2[0]=iterate[list_char2[0]]

        ## two conditions 

        # condition 1
        counter_1=0
        for i in range(1,len(string)):

            if list_char1[i-1]==list_char1[i]:
                list_char1[i]=iterate[list_char1[i]]
                counter_1+=1
            else:
                continue
        ## condition 2
        counter_2=0
        for i in range(1,len(string)):

            if list_char2[i-1]==list_char2[i]:
                list_char2[i]=iterate[list_char2[i]]
                counter_2+=1
            else:
                continue

        
            
        return min(counter_1,counter_2+1)


### Complexity analysis #########
#### Time complexity  O(n) space complexity O(1)

## but i think we have two auxilary space complexity O(m+n) m=len(list_char1),n=len(list_char2)