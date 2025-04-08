def bubbleSort(arr):
    for i in range(len(arr) - 1):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


arr = [23, 53, 19, 329, 128, 3, 20]
print("Unsorted Array:", arr)
bubbleSort(arr)
print("Sorted Array:", arr)
