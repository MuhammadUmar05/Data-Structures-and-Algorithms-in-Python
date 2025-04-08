rows = int(input("Enter no of rows: "))
cols = int(input("Enter no of cols: "))
matrix1 = [
    [int(input(f"Enter element at row {i+1} column {j+1}: ")) for j in range(cols)]
    for i in range(rows)
]
matrix2 = [
    [int(input(f"Enter element at row {i+1} column {j+1}: ")) for j in range(cols)]
    for i in range(rows)
]

sum_matrix = [
    [int(matrix1[i][j] + matrix2[i][j]) for j in range(cols)] for i in range(rows)
]

for row in sum_matrix:
    print(row)


# Application of 2D Arrays in Linear Search
def linearSearch(matrix, target, rows, cols):
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == target:
                return (i, j)
    return (-1, -1)


print("Key found at index:", linearSearch(matrix1, 10, 3, 3))
