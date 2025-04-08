def linearSearch(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


arr = [32, 15, 2, 27, 6]
target = int(input("Enter a target: "))
index = linearSearch(arr, target)

if index != -1:
    print(f"Target found at the index {index}")
else:
    print(f"Target not found in the array")
