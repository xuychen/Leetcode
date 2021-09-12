import sys

x, y, a, b = map(int, sys.stdin.readline().strip().split())

max1 = min(x / a, y / b)
max2 = 0
total = max1 + max2

while max1 > 0:
    max2 += 1
    max1 = min((x-b*max2) / a, (y-a*max2) / b)

    if max1 + max2 > total:
        total = max1 + max2
    elif max1 + max2 < total:
        break

print(total)



