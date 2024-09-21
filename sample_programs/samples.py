def add_arrays(array1, array2):
    # Check if arrays have the same length
    if len(array1) != len(array2):
        return None
    
    # Perform element-wise addition
    result = []
    for i in range(len(array1)):
        result.append(array1[i] + array2[i])
    
    return result

# Ask the user for input and create the first array
array1 = input("Enter the elements of the first array (space-separated): ").split()
array1 = [int(x) for x in array1]

# Ask the user for input and create the second array
array2 = input("Enter the elements of the second array (space-separated): ").split()
array2 = [int(x) for x in array2]

# Call the function and print the result
sum_array = add_arrays(array1, array2)
if sum_array is not None:
    print("Sum of the arrays:", sum_array)
else:
    print("Error: The arrays do not have the same length.")
