import sys
from collections import defaultdict, deque
import heapq

n = input()
max_num = input()
graph = defaultdict(list)
degrees = [0] * n
depth = [-1] * n
hq = []

for _ in range(input()):
    line = sys.stdin.readline().strip().split()
    prev, post = map(int, line)
    graph[prev-1].append(post-1)
    degrees[post-1] += 1
    
print(n, max_num, graph, degrees)

def dfs(node):
    if depth[node] != -1:
        return depth[node]
    if not graph[node]:
        return 0
    
    result = 0
    for next_node in graph[node]:
        result = max(result, dfs(next_node))
        
    depth[node] = result + 1
    return depth[node]

for i in range(n):
    depth[i] = dfs(i)
    
for i in range(n):
    if degrees[i] == 0:
        heapq.heappush(hq, (-depth[i], i))

print(hq)
result = 0
while hq:
    for _ in range(max_num):
        if hq:
            _, node = heapq.heappop(hq)
            for next_node in graph[node]:
                degrees[next_node] -= 1
                print(degrees)
                if degrees[next_node] == 0:
                    heapq.heappush((-depth[next_node], next_node))
                
        print(hq)
    result += 1
    
print(result)
   