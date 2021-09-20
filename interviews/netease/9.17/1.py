import sys
from collections import defaultdict

a_num, b_num = map(int, sys.stdin.readline().strip().split())
id2name = {}
id2act = defaultdict(set)
id2score = defaultdict(int)
result = []

for _ in range(a_num):
    pid, name = sys.stdin.readline().strip().split()
    id2name[int(pid)] = name

for _ in range(b_num):
    pid, aid, score = sys.stdin.readline().strip().split()
    ipid = int(pid)
    id2act[ipid].add(aid)
    id2score[ipid] += int(score)

for pid, value in id2act.items():
    if len(value) >= 2:
        result.append((id2name[pid], id2score[pid]))

for name, score in sorted(result, key=lambda x: (-x[1], x[0])):
    print(name + " " + str(score))