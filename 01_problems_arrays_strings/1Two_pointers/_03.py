def combine(arr1, arr2):
    # ans is the answer list that will store the combined sorted elements
    ans = []
    i = j = 0  # Initialize two pointers for both input arrays

    # Loop until one of the arrays is fully traversed
    while i < len(arr1) and j < len(arr2):
        # Compare the current elements of both arrays
        if arr1[i] < arr2[j]:
            ans.append(arr1[i])  # Add the smaller element to the answer list
            i += 1  # Move the pointer in arr1 forward
        else:
            ans.append(arr2[j])  # Add the smaller element to the answer list
            j += 1  # Move the pointer in arr2 forward

    # If there are remaining elements in arr1, add them to ans
    while i < len(arr1):
        ans.append(arr1[i])
        i += 1

    # If there are remaining elements in arr2, add them to ans
    while j < len(arr2):
        ans.append(arr2[j])
        j += 1

    return ans  # Return the combined sorted list

# Example usage
print(combine([1, 3, 5], [2, 4, 6]))  # Output: [1, 2, 3, 4, 5, 6]
print(combine([1, 2, 3], [4, 5, 6]))  # Output: [1, 2, 3, 4, 5, 6]

"""
Time Complexity: O(n + m), where n and m are the lengths of arr1 and arr2. The function processes each element 
exactly once.

Space Complexity: O(n + m) for the ans list, which contains all the elements from both input arrays.
"""