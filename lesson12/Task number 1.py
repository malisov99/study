import random

def generate_matrix(rows, cols, min_value=-100, max_value=100):
    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(random.randint(min_value, max_value))
        matrix.append(row)
    return matrix

def add_matrices(matrix_1, matrix_2):
    rows = len(matrix_1)
    cols = len(matrix_1[0])

    result = []
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(matrix_1[i][j] + matrix_2[i][j])
        result.append(row)

    return result

rows = 10
cols = 10

matrix_1 = generate_matrix(rows, cols)
matrix_2 = generate_matrix(rows, cols)

matrix_3 = add_matrices(matrix_1, matrix_2)

print("Matrix 1:")
for row in matrix_1:
    print(row)

print("\nMatrix 2:")
for row in matrix_2:
    print(row)

print("\nMatrix 3 (сумма):")
for row in matrix_3:
    print(row)


matrix_1 = generate_matrix(4, 3)
matrix_2 = generate_matrix(4, 3)
matrix_3 = add_matrices(matrix_1, matrix_2)
