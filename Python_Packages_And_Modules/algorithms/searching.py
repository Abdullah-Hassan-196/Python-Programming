
def linear_search(arr, element):
    """
    Linear search implementation.
    
    Parameters:
    arr (list): The list to search in.
    element (int): The value to search for.
    
    Returns:
    int: Index of element in arr if found, -1 otherwise.
    """
    for i in range(len(arr)):
        if arr[i] == element:
            return i
    return -1

def binary_search(arr, element):
    """
    Binary search implementation.
    
    Parameters:
    arr (list): The list to search in (must be sorted).
    element (int): The value to search for.
    
    Returns:
    int: Index of element in arr if found, -1 otherwise.
    """
    start = 0
    end = len(arr) - 1
    while start <= end:
        middle = int((start + end) / 2)
        if arr[middle] == element:
            return middle
        elif arr[middle] > element:
            end = middle - 1
        else:
            start = middle + 1
    return -1


def interpolation_search(arr, element):
    """
    Interpolation search implementation.

    Parameters:
    arr (list): The list to search in (must be sorted).
    element (int): The value to search for.

    Returns:
    int: Index of element in arr if found, -1 otherwise.
    """
    # arr should be sorted for interpolationSearch
    
    lo, hi = 0, len(arr) - 1
    while lo <= hi and arr[lo] <= element <= arr[hi]:
        pos = lo + ((hi - lo) // (arr[hi] - arr[lo])) * (element - arr[lo])
        if arr[pos] == element:
            return pos
        elif arr[pos] < element:
            lo = pos + 1
        else:
            hi = pos - 1
    return -1

def exponential_search(arr, element):
    """
    Exponential search implementation.

    Parameters:
    arr (list): The list to search in (must be sorted).
    element (int): The value to search for.

    Returns:
    int: Index of element in arr if found, -1 otherwise.
    """
    
    # arr should be sorted for exponentialSearch

    n = len(arr)
    if n == 0:
        return -1
    
    # If the element is at the first position
    if arr[0] == element:
        return 0
    
    # Find the range for binary search
    i = 1
    while i < n and arr[i] <= element:
        i *= 2

    # Perform binary search in the found range
    return binary_search(arr[:min(i, n)], element)



def jump_search(arr, element):
    """
    Jump search implementation.
    
    Parameters:
    arr (list): The list to search in (must be sorted).
    element (int): The value to search for.
    
    Returns:
    int: Index of element in arr if found, -1 otherwise.
    """
    n = len(arr)
    step = int(n ** 0.5)
    prev = 0
    while arr[min(step, n) - 1] < element:
        prev = step
        step += int(n ** 0.5)
        if prev >= n:
            return -1
    while arr[prev] < element:
        prev += 1
        if prev == min(step, n):
            return -1
    if arr[prev] == element:
        return prev
    return -1

def main():
    array=[-4,2,4,5,6,9,10]
    print("Array for Seaching Algorithms: ",array)
    print("Linear Search: ",linear_search(array,4))
    print("Linear Search: ",linear_search(array,8))
    print("Binary Search: ",binary_search(array,5))
    print("Binary Search: ",binary_search(array,1))
    print("Interpolation Search: ",interpolation_search(array,9))
    print("Interpolation Search: ",interpolation_search(array,-2))
    print("Exponential Search: ",exponential_search(array,6))
    print("Exponential Search: ",exponential_search(array,20))
    print("Jump Search: ",jump_search(array,2))
    print("Jump Search: ",jump_search(array,1))
    print()    


main()