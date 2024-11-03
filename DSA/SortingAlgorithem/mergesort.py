def merge_sort(arr):
    if len(arr) > 1:
        # Step 1: Divide the array into two halves
        mid = len(arr) // 2  # Find the middle point
        left_half = arr[:mid]  # Divide the array elements into two halves
        right_half = arr[mid:]

        # Step 2: Recursively sort both halves
        merge_sort(left_half)
        merge_sort(right_half)

        # Step 3: Merge the sorted halves
        i = j = k = 0

        # Copy data to temporary arrays left_half[] and right_half[]
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Check if any elements were left in the left_half
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        # Check if any elements were left in the right_half
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

    return arr  # Return the sorted array

# Example usage:
arr = [38, 27, 43, 3, 9, 82, 10]
sorted_arr = merge_sort(arr)
print("Sorted array:", sorted_arr)
