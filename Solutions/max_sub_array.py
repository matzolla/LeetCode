def max_sub_array(arr,low,mid,high):

    curr_sum=0
    left_sum= -float('inf')
    for idx in range(mid,low-1,-1):

        curr_sum+=arr[idx]

        if curr_sum> left_sum:

            left_sum= curr_sum

    curr_sum=0
    right_sum=-float('inf')

    for idx in range(mid,high):

        curr_sum+=arr[idx]

        if curr_sum> right_sum:

            right_sum=curr_sum

    return max(right_sum+left_sum-arr[mid],left_sum,right_sum)



def cross_max(arr,low,high):

    if low>high: return

    if low==high: return arr[low]

    mid= (low+high)//2


    return max(cross_max(arr,low,mid-1),cross_max(arr,mid+1,high),max_sub_array(arr,low,mid,high))


## time complexity O(nlogn)
## space complexity O(1)
