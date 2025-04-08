def binarySearch(arr, target):
    i, j = 0, len(arr) - 1
    while i <= j:
        mid = (i + j) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            j = mid - 1
        else:
            i = mid + 1
    return -1


arr = [17, 24, 33, 39, 51]
target = int(input("Enter a target: "))
index = binarySearch(arr, target)

if index != -1:
    print(f"Target found at the index {index}")
else:
    print(f"Target not found in the array")
