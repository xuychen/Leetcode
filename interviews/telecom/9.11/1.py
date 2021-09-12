import sys
from collections import defaultdict

string = sys.stdin.readline().strip()
counter = defaultdict(int)
start = 0
result = 0

for i, char in enumerate(string):
    counter[char] += 1
    while counter[char] > 1:
        counter[string[start]] -= 1
        start += 1

    result = max(i-start+1, result)

print(result)