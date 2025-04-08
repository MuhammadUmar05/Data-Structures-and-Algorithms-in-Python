def selectionSort(arr):
    for i in range(len(arr) - 1):
        smallestIndex = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[smallestIndex]:
                smallestIndex = j
        arr[i], arr[smallestIndex] = arr[smallestIndex], arr[i]


arr = [23, 53, 19, 329, 128, 3, 20]
selectionSort(arr)
print(arr)
