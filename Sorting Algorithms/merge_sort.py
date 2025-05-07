def merge_sort(arr, start, end):
    if start < end:
        mid = (start + end) // 2
        merge_sort(arr, start, mid)  # left half
        merge_sort(arr, mid + 1, end)  # right half
        merge(arr, start, end, mid)


def merge(arr, start, end, mid):
    i = start
    j = mid + 1
    temp = []
    while i <= mid and j <= end:
        if arr[i] <= arr[j]:
            temp.append(arr[i])
            i += 1
        else:
            temp.append(arr[j])
            j += 1

    while i <= mid:
        temp.append(arr[i])
        i += 1
    while j <= mid:
        temp.append(arr[j])
        j += 1

    for idx in range(len(temp)):
        arr[idx + start] = temp[idx]


arr = [24, 7, 12, 15, 4, 9, 17, 29]
print(f"Unsorted Array: {arr}")
merge_sort(arr, 0, len(arr) - 1)
print(f"Sorted Array: {arr}")
