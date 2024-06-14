#!/usr/bin/python3
def find_peak(arr):
    if arr is None or len(arr) == 0:
        return None
    n = len(arr)
    
    if n == 1:
        return arr[0]
    
    left, right = 0, n - 1
    
    while left < right:
        mid = left + (right - left) // 2
        
        if arr[mid] < arr[mid + 1]:
            left = mid + 1
        else:
            right = mid
            
    return arr[left]

# Example usage
arr = [4, 2, 1, 2, 3, 1]
print(find_peak(arr))
arr = [2, 2, 2]
print(find_peak(arr))
arr = [4, 2, 1, 2, 2, 2, 3, 1]
print(find_peak(arr))
arr = [-2, -4, 2, 1]
print(find_peak(arr))