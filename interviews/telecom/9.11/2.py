import sys

waters = input()
if waters <= 1:
    print(waters)
else:
    bottles = [1, 5, 10, 20, 50, 100]
    num_bottles = len(bottles)
    dp = [[0] * (waters+1) for _ in range(num_bottles)]
    dp[0][0] = 1
    result = 0

    for i in range(num_bottles):
        for j in range(waters+1):
            for k in range(i, num_bottles):
                bottle = bottles[k]
                if j + bottle <= waters:
                    dp[k][j+bottle] += dp[i][j]

    for i in range(num_bottles):
        result += dp[i][waters]

    print(result)