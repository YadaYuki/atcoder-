from collections import deque

N,M = map(int,input().split())
graph = [[] for _ in range(N)]

for _ in range(M):
    A,B = map(int,input().split())
    graph[A-1].append(B-1)
    graph[B-1].append(A-1)

cost_to_node = [-1] * N
shortest_paths_pattern_num = [0] * N
cost_to_node[0] = 0
shortest_paths_pattern_num[0] = 1

queue = deque([0])


while len(queue) > 0:
    node = queue.popleft()
    for next_node in graph[node]:
        if cost_to_node[next_node] == -1:
            cost_to_node[next_node] = cost_to_node[node] + 1
            shortest_paths_pattern_num[next_node] = shortest_paths_pattern_num[node]
            queue.append(next_node)
        elif cost_to_node[next_node] == cost_to_node[node] + 1:
            shortest_paths_pattern_num[next_node] += shortest_paths_pattern_num[node]
            shortest_paths_pattern_num[next_node] %= 1000000007


print(shortest_paths_pattern_num[-1])