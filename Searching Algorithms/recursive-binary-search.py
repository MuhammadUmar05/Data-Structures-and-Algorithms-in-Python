def binarySearch(arr, target, i, j):
    if i <= j:
        mid = (i + j) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            return binarySearch(arr, target, i, mid - 1)
        else:
            return binarySearch(arr, target, mid + 1, j)
    return -1


arr = [17, 24, 33, 39, 51]
target = int(input("Enter a target: "))
index = binarySearch(arr, target)

if index != -1:
    print(f"Target found at the index {index}")
else:
    print(f"Target not found in the array")
