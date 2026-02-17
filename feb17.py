# Write a program to find the maximum and minimum values present in a given array of integers.

def find_max_min(arr):
    if not arr:
        return None, None  # Handle empty array
    
    max_value = arr[0]
    min_value = arr[0]
    
    for num in arr:
        if num > max_value:
            max_value = num
        if num < min_value:
            min_value = num
    
    return max_value, min_value


# Example usage
numbers = [12, 45, 7, 89, 23, -4, 67]
maximum, minimum = find_max_min(numbers)

print("Array:", numbers)
print("Maximum value:", maximum)
print("Minimum value:", minimum)
