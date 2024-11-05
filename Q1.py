import matplotlib.pyplot as plt
import timeit
import random

def merge(arr, left, mid, right):
    n1 = mid - left + 1
    n2 = right - mid

    # Create temp arrays
    L = [0] * n1
    R = [0] * n2

    # Copy data to temp arrays L[] and R[]
    for i in range(n1):
        L[i] = arr[left + i]
    for j in range(n2):
        R[j] = arr[mid + 1 + j]

    i = 0  # Initial index of first subarray
    j = 0  # Initial index of second subarray
    k = left  # Initial index of merged subarray

    # Merge the temp arrays back
    # into arr[left..right]
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    # Copy the remaining elements of L[],
    # if there are any
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    # Copy the remaining elements of R[], 
    # if there are any
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

def merge_sort(arr, left, right):
    if left < right:
        mid = (left + right) // 2

        merge_sort(arr, left, mid)
        merge_sort(arr, mid + 1, right)
        merge(arr, left, mid, right)




# Function to sort array using insertion sort
def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# A utility function to print array of size n
def printArray(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()


if __name__ == "__main__":
    merge_times = []
    insertion_times = []
    input_sizes = range(1, 201)
    for i in range(1,201):
        merge_time = 0
        insertion_time = 0
        for x in range(200):
            merge_arr = random.sample(range(1,201),i)
            insertion_arr = merge_arr[:]
            merge_start = timeit.default_timer()
            merge_sort(merge_arr, 0, len(merge_arr) - 1)
            merge_end = timeit.default_timer()
            merge_difference = merge_end - merge_start
            merge_time += merge_difference

            insertion_start = timeit.default_timer()
            insertionSort(insertion_arr)
            insertion_end = timeit.default_timer()
            insertion_difference = insertion_end - insertion_start
            insertion_time += insertion_difference

        merge_times.append(merge_time / 200)
        insertion_times.append(insertion_time / 200)



    plt.figure(figsize=(10, 6))
    plt.plot(input_sizes, merge_times, label="Merge Sort Time", color="blue")
    plt.plot(input_sizes, insertion_times, label="Insertion Sort Time", color="red")
    plt.xlabel("Input Size")
    plt.ylabel("Time (seconds)")
    plt.title("Merge Sort vs Insertion Sort Time Complexity")
    plt.legend()
    plt.grid(True)
    plt.show()
