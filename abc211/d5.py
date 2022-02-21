from collections import deque

N,M = map(int,input().split())

graph = [[] for _ in range(N)]

for _ in range(M):
    A,B = map(int,input().split())
    graph[A-1].append(B-1)
    graph[B-1].append(A-1)

BIG = 10**9
MOD = 10**9 + 7
cost_to_nodes = [BIG]*N


queue = deque([0])
cost_to_nodes[0] = 0
shortest_paths_pattern_num = [0]*N
shortest_paths_pattern_num[0] = 1

while len(queue) > 0:
    node = queue.popleft()
    cost_to_node = cost_to_nodes[node]
    for next_node in graph[node]:
        if cost_to_nodes[next_node] == BIG:
            cost_to_nodes[next_node] = cost_to_node + 1
            shortest_paths_pattern_num[next_node] = shortest_paths_pattern_num[node]
            queue.append(next_node)
        elif cost_to_nodes[next_node] == cost_to_node + 1:
            shortest_paths_pattern_num[next_node] += shortest_paths_pattern_num[node]
            shortest_paths_pattern_num[next_node] %= MOD
        


print(shortest_paths_pattern_num[N-1])