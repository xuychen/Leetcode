import sys

nodes, root = map(int, sys.stdin.readline().strip().split())
colors = map(int, sys.stdin.readline().strip().split())
graph = [[] for _ in range(nodes)]
answer = [0] * nodes
root -= 1

for _ in range(nodes-1):
    start, end = map(int, sys.stdin.readline().strip().split())
    graph[start-1].append(end-1)

def dfs(node):
    result = 0
    for next_node in graph[node]:
        result += (colors[node] ^ colors[next_node]) + dfs(next_node)

    answer[node] = result
    return result

dfs(root)
print(" ".join(map(str, answer)))