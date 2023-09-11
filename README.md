# LeetCode
Questions and Answers , LeetCode preparatory personal repo 
Back to back coding interview  (level medium)

```python
# example functions binary search

def binary_search(array, value):
    left=0
    right=len(array)-1
    while left < right:
        mid= (left+right)//2
        if array[mid]==value:
           return mid
        if array[mid] < value:
           left= mid+1
        else:
           right= mid-1     
```

