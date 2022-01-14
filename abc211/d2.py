from  collections import deque

N,M =map(int, input().split())

graph = [[] for _ in range(N)]


for _ in range(M):
    a,b = map(int, input().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)

MOD = 10**9+7
# bfs
cost_to_node = [-1] * N

path_pattern_to_node = [0] * N
path_pattern_to_node[0] = 1
Q = deque([0])

while len(Q) > 0:
    node = Q.pop()
    for node_next_to in graph[node]:
        if cost_to_node[node_next_to] == -1:
            cost_to_node[node_next_to] = cost_to_node[node] + 1
            Q.appendleft(node_next_to)
            path_pattern_to_node[node_next_to] = path_pattern_to_node[node]
        elif cost_to_node[node_next_to] == cost_to_node[node] + 1:
            path_pattern_to_node[node_next_to] += path_pattern_to_node[node] % MOD

print(path_pattern_to_node[-1])

