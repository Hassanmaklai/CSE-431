import matplotlib.pyplot as plt
import timeit
import random
import numpy as np
from Q1 import merge_sort
from Q1 import insertionSort

# Merge function
def merge(arr, left, mid, right):
    n1 = mid - left + 1
    n2 = right - mid
    L = [0] * n1
    R = [0] * n2
    for i in range(n1):
        L[i] = arr[left + i]
    for j in range(n2):
        R[j] = arr[mid + 1 + j]
    i, j, k = 0, 0, left
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

# Merge sort modified to use insertion sort for small partitions
def hybrid_sort(arr, left, right, k):
    if right - left + 1 <= k:
        insertionSort(arr, left, right)
    else:
        mid = (left + right) // 2
        hybrid_sort(arr, left, mid, k)
        hybrid_sort(arr, mid + 1, right, k)
        merge(arr, left, mid, right)

# Insertion sort, modified to sort between left and right indices
def insertionSort(arr, left, right):
    for i in range(left + 1, right + 1):
        key = arr[i]
        j = i - 1
        while j >= left and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Function to test various values of k on an array of size 200
def test_hybrid_sort():
    k_values = range(2, 200, 2)  # Testing a range of k values
    size = 200  # Fixed array size
    results = {'merge': 0, 'insertion': 0, 'hybrid': {}}

    # Testing Hybrid Sort for various k values
    for k in k_values:
        hybrid_times = 0
        for _ in range(100):  # Averaging over 100 runs
            arr = random.sample(range(1, size * 10), size)
            hybrid_arr = arr[:]
            
            # Hybrid Sort
            hybrid_start = timeit.default_timer()
            hybrid_sort(hybrid_arr, 0, len(hybrid_arr) - 1, k)
            hybrid_end = timeit.default_timer()
            hybrid_times += hybrid_end - hybrid_start

        # Average time for hybrid sort with current k
        results['hybrid'][k] = hybrid_times / 100

    # Baseline Merge Sort
    merge_times = 0
    for _ in range(100):
        arr = random.sample(range(1, size * 10), size)
        merge_arr = arr[:]
        merge_start = timeit.default_timer()
        merge_sort(merge_arr, 0, len(merge_arr) - 1)
        merge_end = timeit.default_timer()
        merge_times += merge_end - merge_start
    results['merge'] = merge_times / 100

    # Baseline Insertion Sort
    insertion_times = 0
    for _ in range(100):
        arr = random.sample(range(1, size * 10), size)
        insertion_arr = arr[:]
        insertion_start = timeit.default_timer()
        insertionSort(insertion_arr, 0, len(insertion_arr) - 1)
        insertion_end = timeit.default_timer()
        insertion_times += insertion_end - insertion_start
    results['insertion'] = insertion_times / 100
    
    the_list = [results['hybrid'][k] for k in k_values]
    minimum = k_values[np.argmin(the_list)]
    print(minimum)
    # Plotting
    plt.figure(figsize=(10, 6))
    plt.plot(k_values, [results['hybrid'][k] for k in k_values], label="Hybrid Sort (n=200)")
    plt.axhline(y=results['merge'], color="blue", linestyle="--", label="Merge Sort")
    plt.axhline(y=results['insertion'], color="red", linestyle="--", label="Insertion Sort")
    plt.xlabel("Value of k")
    plt.ylabel("Time (seconds)")
    plt.title("Hybrid Sort vs Merge Sort vs Insertion Sort (n=200)")
    plt.legend()
    plt.grid(True)
    plt.show()

# Run the test
test_hybrid_sort()
