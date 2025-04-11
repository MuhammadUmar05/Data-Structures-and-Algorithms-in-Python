def insertionSort(arr):
    for i in range(1, len(arr)):
        current = arr[i]
        prev = i - 1
        while prev >= 0 and arr[prev] > current:
            arr[prev + 1] = arr[prev]
            prev -= 1
        arr[prev + 1] = current


arr = [5, 2, 9, 1, 5, 6]
print("Unsorted Array:", arr)
insertionSort(arr)
print("Sorted Array:", arr)
