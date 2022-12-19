## let's try to implement the monotonic stack 
## to see
## [2, 3, 7, 11, 5, 17, 19]
## completing the monotonic stack =[2,3,5,17,19]
def monotonic_stack(arr):

    stack=[]
    for i in range(len(arr)):

        while len(stack) and stack[-1]> arr[i]:

            stack.pop()

        stack.append(arr[i])
    return stack



print(monotonic_stack([2, 3, 7, 11, 5, 17, 19]))

### Next greater number
def next_greater(arr):

    stack=[]
    result=[0]*len(arr)

    for idx in range(len(arr)):

        while len(stack) and arr[stack[-1]]<arr[idx]:

            item=stack.pop()
            result[item]=arr[idx]

        stack.append(idx)

    
    return result

print(next_greater([2, 3, 7, 11, 5, 17, 19]))
    