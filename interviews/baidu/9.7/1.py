import sys

n, w = map(int, sys.stdin.readline().strip().split())
weights = []
energys = []
dp = [float('-inf')] * (w + 1)
dp[0] = 0

for _ in range(n):
    weight, energy = map(int, sys.stdin.readline().strip().split())
    weights.append(weight)
    energys.append(energy)


for j in range(n):
    for _ in range(2):
        for i in range(w, -1, -1):
            if i+weights[j] <= w:
                dp[i+weights[j]] = max(dp[i+weights[j]], energys[j]+dp[i])

print(max(dp))
