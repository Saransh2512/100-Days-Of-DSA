# Given an array of integers, count the frequency of each distinct element and print the result.

def count_frequencies(arr):
    freq = {}
    
    for num in arr:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    
    for key, value in freq.items():
        print(f"{key} -> {value}")

# Example
arr = [1, 2, 2, 3, 1, 4, 2]
count_frequencies(arr)
