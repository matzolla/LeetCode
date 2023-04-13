"""
Here i'm trying to implement the count sort algorithm
to sort an array 

example [2,0,4,5,3,4,6]

residu= [0,0,0,0,0,0,0]

## second step
residu=[1,0,1,1,2,1,1]

## third step

residu=[1,1,2,3,5,6,7]

output: [0,2,3,4,4,5,6]
"""


class solution(object):

    def count_sort(self, array):

        # Input array
        # output sorted array


        # initializing a residu

        residu= [0]*(max(array)+1)

        output=[0]*len(array)

        ## assigning a value 1 to all existing inetegers

        for i in array:

            residu[i]+=1  # time complexity O(n)  n= len of array

        ## computing the cumulative frequency

        for j in range(1, len(residu)):

            residu[j]+=residu[j-1]

        ### sorted values

        for k in array:

            residu[k]-=1

            output[residu[k]]=k


        return output



### Complexity analysis ####
## time complexity O(n+m) where n=len(array), m=len(residu)

# https://www.programiz.com/dsa/counting-sort

## space complexity O(m) (but we have many auxilary space complexity)

"""
residu=[0 0 0 0 0 0 0 0] #initially
output=[0 0 0 0 0 0 0]
residu=[1 0 1 1 2 1 1 1]

## after cumulatif frequency
array=[2,0,4,5,3,4,6]
residu=[1 1 2 3 5 6 7 8]
output=[0 2 3 4 4 5 6 ]

"""

