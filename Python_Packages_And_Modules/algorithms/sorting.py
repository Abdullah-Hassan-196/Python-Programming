def bubble_sort(arr):
    """
    Bubble sort implementation.
    
    Parameters:
    arr (list): The list to be sorted.
    
    Returns:
    list: Sorted list.
    """
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def selection_sort(arr):
    """
    Selection sort implementation.
    
    Parameters:
    arr (list): The list to be sorted.
    
    Returns:
    list: Sorted list.
    """
    
    size=len(arr)
    for step in range(size):
        min_idx = step

        for i in range(step + 1, size):

            # to sort in descending order, change > to < in this line
            # select the minimum element in each loop
            if arr[i] < arr[min_idx]:
                min_idx = i

        # put min at the correct position
        (arr[step], arr[min_idx]) = (arr[min_idx], arr[step])
        
    return arr
    


def insertion_sort(arr):
    """
    Insertion sort implementation.
    
    Parameters:
    arr (list): The list to be sorted.
    
    Returns:
    list: Sorted list.
    """
    for step in range(1, len(arr)):
        key = arr[step]
        j = step - 1

        # Compare key with each element on the left of it until an element smaller than it is found
        # For descending order, change key<array[j] to key>array[j].
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j = j - 1

        # Place key at after the element just smaller than it.
        arr[j + 1] = key

    return arr

def merge_sort(arr):
    """
    Merge sort implementation.
    
    Parameters:
    arr (list): The list to be sorted.
    
    Returns:
    list: Sorted list.
    """
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

    return arr

def quick_sort(arr):
    """
    Quick sort implementation.
    
    Parameters:
    arr (list): The list to be sorted.
    
    Returns:
    list: Sorted list.
    """
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        left = [x for x in arr[1:] if x <= pivot]
        right = [x for x in arr[1:] if x > pivot]
        return quick_sort(left) + [pivot] + quick_sort(right)


def main():
    arr=[2,-1,0,8,6,-3, 7,6]
    print("Array to be sorted: ", arr)
    print("Bubble Sort :", bubble_sort(arr))
    print("Selection Sort: ", selection_sort(arr))
    print("Insertion Sort: ", insertion_sort(arr))
    print("Merge Sort: ",merge_sort(arr))
    print("Quick Sort: ",quick_sort(arr))
    print()
main()