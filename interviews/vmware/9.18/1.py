import sys

left, right = map(int, sys.stdin.readline().strip().split())
primes = [2,3,5,7]
count = 0

for num in range(11, right+1, 2):
    prime_flag = True
    for prime in primes:
        if num % prime == 0:
            prime_flag = False
            break

    if prime_flag:
        primes.append(num)
        if num >= left and str(num).count("1") >= 1:
            count += 1

print(count)