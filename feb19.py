#  Given an array of integers, find two elements whose sum is closest to zero.

def two_sum_closest_to_zero(arr):
    arr.sort()
    left = 0
    right = len(arr) - 1
    
    min_sum = float('inf')
    min_pair = (None, None)
    
    while left < right:
        current_sum = arr[left] + arr[right]
        
        if abs(current_sum) < abs(min_sum):
            min_sum = current_sum
            min_pair = (arr[left], arr[right])
        
        if current_sum < 0:
            left += 1
        else:
            right -= 1
    
    return min_pair

# Example
arr = [-8, -66, -60, 10, 15, 20]
print(two_sum_closest_to_zero(arr))
