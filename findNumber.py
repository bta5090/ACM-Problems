import math

def findNumber(arr, k):
    
    arr.sort()
    x = 0
    y = len(arr) - 1
    
    while (x <= y):
        
        mid = math.floor((x + y) / 2)
        if arr[mid] == k:
            return "YES"
        elif arr[mid] > k:
            y = mid - 1
            new = []
            new = arr[:mid]
            findNumber(arr[0:mid], k)
        elif arr[mid] < k:
            x = mid
            new = []
            new = arr[mid:]
            findNumber(arr[mid:], k)
            
    return "NO"
