n = input()

result = []
max_iter = int((2 * n) ** 0.5)

for i in range(max_iter, 1, -1):
    if i & 1:
        center = n / i
        if center * i == n and center - i / 2 >= 1:
            result.append(range(center-i/2, center+i/2+1))
    else:
        center = n / i + 1
        if n % i * 2 == i and center - i / 2 >= 1:
            result.append(range(center-i/2, center+i/2))

for line in result:
    print(" ".join(map(str, line)))
