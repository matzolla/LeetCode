# LeetCode

Questions and Answers , LeetCode preparatory personal repo 
Back to back coding interview  (level `medium` to `hard`)
1. $2022$ Interviewed at Google twice (AI residency role and SWE site reliability role) rejected in first round straight!!!
2. $2023$ Interviewed once at Meta (AI residency). Rejected at final round cause the residency programm closed
3. $2024$ 

Sample codes
```python
# example functions binary search
# time complexity O(logn)

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

Will definitely joint one of the `MAANG`
