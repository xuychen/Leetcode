import sys

inodes, hnodes, onodes = map(int, sys.stdin.readline().strip().split())
tmp = sys.stdin.readline().strip().split()
epochs, lr = int(tmp[0]), float(tmp[1])
data_size = input()

ih_matrix = []
ho_matrix = []
data = []
result = []

for _ in range(hnodes):
    ih_matrix.append(map(float, sys.stdin.readline().strip().split()))

for _ in range(onodes):
    ho_matrix.append(map(float, sys.stdin.readline().strip().split()))

for _ in range(data_size):
    data.append(map(float, sys.stdin.readline().strip().split()))

for _ in range(data_size):
    result.append(map(float, sys.stdin.readline().strip().split()))
