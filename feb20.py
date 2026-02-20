# Given an array of integers, find two elements whose sum is closest to zero.

def two_sum_closest_to_zero(arr):
    arr.sort()
    left = 0
    right = len(arr) - 1

    min_sum = float('inf')
    best_pair = (None, None)

    while left < right:
        current_sum = arr[left] + arr[right]

        if abs(current_sum) < abs(min_sum):
            min_sum = current_sum
            best_pair = (arr[left], arr[right])

        if current_sum < 0:
            left += 1
        else:
            right -= 1

    return best_pair


# Test
arr = [-8, -3, 2, 4, 5]
print("Pair closest to zero:", two_sum_closest_to_zero(arr))