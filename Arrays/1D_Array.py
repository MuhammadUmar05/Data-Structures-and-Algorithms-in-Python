def reverse_array(arr):
    i, j = 0, len(arr) - 1
    while i < j:
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j -= 1


arr = []
n = int(input("Enter the length of an array: "))

for i in range(n):
    num = int(input(f"Enter the element at index {i}: "))
    arr.append(num)

minNum = arr[0]
for i in range(1, len(arr)):
    if minNum > arr[i]:
        minNum = arr[i]

print(arr)
print(f"Minimum number in an array is {minNum}")

sum = 0
for i in range(len(arr)):
    sum += arr[i]

print(f"The sum of array {arr} is: {sum}")
