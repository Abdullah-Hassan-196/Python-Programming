import time
import numpy as np
import algorithms.sorting as sorting
import algorithms.searching as searching

def generate_data(size):
    return np.random.randint(0, 1000, size)

def measure_sorting_performance():
    sizes = [1000, 10000, 50000, 100000]
    sorting_algorithms = {
        'Bubble Sort': sorting.bubble_sort,
        'Merge Sort': sorting.merge_sort,
        # Add other sorting algorithms here
    }

    for size in sizes:
        data = generate_data(size)
        print(f"Array size: {size}")
        for algorithm_name, algorithm_func in sorting_algorithms.items():
            start_time = time.time()
            sorted_data = algorithm_func(data)
            execution_time = time.time() - start_time
            print(f"{algorithm_name}: {execution_time:.6f} seconds")

def measure_searching_performance():
    sizes = [1000, 10000, 50000, 100000]

    searching_algorithms = {
        'Linear Search': searching.linear_search,
        'Binary Search': searching.binary_search,
        'Interpolation Search': searching.interpolation_search,
        'Exponential Search': searching.exponential_search,
        'Jump Search': searching.jump_search

    }

    for size in sizes:
        sorted_data = np.sort(generate_data(size))
        unsorted_data = generate_data(size)
        print(f"Array size: {size}")
        for algorithm_name, algorithm_func in searching_algorithms.items():
            start_time = time.time()
            algorithm_func(sorted_data, sorted_data[size // 2])  # Search for an element in the middle
            execution_time_sorted = time.time() - start_time
            print(f"{algorithm_name} (Sorted): {execution_time_sorted:.6f} seconds")

            start_time = time.time()
            algorithm_func(unsorted_data, sorted_data[size // 2])  # Search for an element in the middle
            execution_time_unsorted = time.time() - start_time
            print(f"{algorithm_name} (Unsorted): {execution_time_unsorted:.6f} seconds")

# Measure sorting performance
print("Sorting Algorithm Performance")
measure_sorting_performance()

# Measure searching performance
print("\nSearching Algorithm Performance")
measure_searching_performance()
