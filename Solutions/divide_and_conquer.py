"""
Time complexity O(nlogn)
merge sort using devide and conquer 
"""

def merge_sort(arr,left,right):

    if left<right:

        mid= (left+right)//2

        merge_sort(arr,left,mid)
        merge_sort(arr,mid+1,right)
        
        merge(arr,mid)




def merge(arr,mid):

    k=0

    left_array=arr[: mid]
    right_array=arr[mid: ]

    left_pointer=0
    right_pointer=0


    while left_pointer< len(left_array) and right_pointer< len(right_array):

        if left_array[left_pointer]< right_array[right_pointer]:
            arr[k]=left_array[left_pointer]

            left_pointer+=1
        else:
            arr[k]=right_array[right_pointer]

            right_pointer+=1
        k+=1
    
    while left_pointer< len(left_array):

        arr[k]=left_array[left_pointer]
        left_pointer+=1
        k+=1

    while right_pointer< len(right_array):

        arr[k]=right_array[right_pointer]
        right_pointer+=1
        k+=1




array = [6, 5, 12, 10, 9, 1]

merge_sort(array,0,len(array))

print(array)