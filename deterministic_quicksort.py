import time
from randomized_quicksort import randomized_quicksort

def deterministic_partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def deterministic_quicksort(arr, low, high):
    if low < high:
        pi = deterministic_partition(arr, low, high)
        deterministic_quicksort(arr, low, pi - 1)
        deterministic_quicksort(arr, pi + 1, high)

if __name__ == "__main__":
    array = [10, 7, 8, 9, 1, 5] * 1000  # Increase array size for meaningful comparisons

    # Randomized Quicksort Timing
    start = time.time()
    randomized_quicksort(array.copy(), 0, len(array) - 1)
    end = time.time()
    print(f"Randomized Quicksort Time: {end - start:.6f} seconds")

    # Deterministic Quicksort Timing
    start = time.time()
    deterministic_quicksort(array.copy(), 0, len(array) - 1)
    end = time.time()
    print(f"Deterministic Quicksort Time: {end - start:.6f} seconds")
