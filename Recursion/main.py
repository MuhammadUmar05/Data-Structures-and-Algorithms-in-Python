# recursion
def printNums(n):
    if n <= 0:
        return
    print(end=f"{n} ")
    printNums(n - 1)


def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)


def sum(n):
    if n == 1:
        return 1
    return n + sum(n - 1)


def fibonacci(n):
    if n == 0 or n == 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


def isSorted(arr, n):
    if n == 0 or n == 1:
        return True
    return arr[n - 1] >= arr[n - 2] and isSorted(arr, n - 1)


print(f"Factorial of 7 is {factorial(7)}")
print(f"sum of first five numbers is {sum(5)}")
print("7th fibonacci term is", fibonacci(7))
arr = [1, 2, 3, 6, 5]
print("is given array sorted??", isSorted(arr, 5))
