import sys

matrix = []
n_rows, n_cols, k = map(int, sys.stdin.readline().strip().split())

for _ in range(n_rows):
    matrix.append(map(int, sys.stdin.readline().strip().split()))

sum_matrix = [[0] * n_cols for _ in range(n_rows)]
sum_matrix[0][0] = matrix[0][0]

for i in range(1, n_cols):
    sum_matrix[0][i] = sum_matrix[0][i-1] + matrix[0][i]
for i in range(1, n_rows):
    sum_matrix[i][0] = sum_matrix[i-1][0] + matrix[i][0]

for i in range(1, n_rows):
    for j in range(1, n_cols):
        sum_matrix[i][j] = sum_matrix[i-1][j] + sum_matrix[i][j-1] - sum_matrix[i-1][j-1] +  matrix[i][j]

result = sum_matrix[k-1][k-1]
for i in range(k, n_cols):
    result = max(result, sum_matrix[k-1][i] - sum_matrix[k-1][i-k])
for i in range(k, n_rows):
    result = max(result, sum_matrix[i][k-1] - sum_matrix[k-i][k-1])

for i in range(k, n_rows):
    for j in range(k, n_cols):
        result = max(result, sum_matrix[i][j] - sum_matrix[i-k][j] - sum_matrix[i][j-k] + sum_matrix[i-k][j-k])

print(result)
