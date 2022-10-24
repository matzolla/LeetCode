## code training day 1 18/04/2022
"""6 months training algorithm challenge
"""

def array_sort_inplace(arr):
    """sorting an array in place
     input--> an array
     output--> the array sorted in place
     
     example: Input-->[1,3,4,7,0,]
     
     output: ----->[0,1,3,4,7]"""

    for i in range(1,len(arr)):
        value=arr[i] ##taking the input
        j=i-1  ## want to compare with the previously taken inputs

        while (j>=0 and value<arr[j]):
            arr[j+1]=arr[j]
            j-=1
        

        arr[j+1]=value

    return arr


####testing example###########

print(array_sort_inplace([31, 41, 59, 26, 41, 58]))
                        