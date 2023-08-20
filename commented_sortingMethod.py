
# Bubble Sort Implementation

# Define the bubble_sort function
def bubble_sort(arr):
    # Get the length of the array
    n = len(arr)
    
    # Outer loop iterates over the entire array
    for i in range(n):
        # Inner loop iterates from the start of the array to the end minus the sorted portion
        for j in range(0, n-i-1):
            # If the current element is greater than the next element, swap them
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    # Return the sorted array
    return arr

# Selection Sort Implementation

# Define the selection_sort function
def selection_sort(arr):
    # Get the length of the array
    n = len(arr)
    
    # Outer loop iterates over the entire array
    for i in range(n):
        # Assume the current index is the minimum
        min_idx = i
        
        # Inner loop iterates over the unsorted portion of the array
        for j in range(i+1, n):
            # If the element at the current minimum index is greater than the current element, update the minimum index
            if arr[min_idx] > arr[j]:
                min_idx = j
        
        # Swap the element at the current index with the element at the minimum index
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    # Return the sorted array
    return arr

# Test the sorting algorithms
# This ensures that the testing code only runs when this script is executed directly, and not when imported as a module
if __name__ == "__main__":
    # Define a list to be sorted
    ls = [8, 3, 5, 2, 9, 1]
    
    # Print the result of the bubble sort
    print("Bubble Sorted List:", bubble_sort(ls.copy()))
    
    # Print the result of the selection sort
    print("Selection Sorted List:", selection_sort(ls.copy()))
