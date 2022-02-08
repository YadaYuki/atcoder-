from collections import deque
N,M = map(int,input().split())
graph = [[] for _ in range(N)]
for _ in range(M):
    A,B = map(int,input().split())
    graph[A-1].append(B-1)
    graph[B-1].append(A-1)

MOD = 10 ** 9 + 7
BIG = 10 ** 10
Q = deque([0])

minimum_cost_to_node = [BIG for _ in range(N)]
patterns_num_of_shortest_paths = [0 for _ in range(N)]
patterns_num_of_shortest_paths[0] = 1
minimum_cost_to_node[0] = 0

while len(Q) > 0:
    town = Q.popleft()
    for next_town in graph[town]:
        if minimum_cost_to_node[next_town] == BIG:
            minimum_cost_to_node[next_town] = minimum_cost_to_node[town] + 1
            patterns_num_of_shortest_paths[next_town] = patterns_num_of_shortest_paths[town]
            Q.append(next_town)
        else:
            if minimum_cost_to_node[next_town] == minimum_cost_to_node[town] + 1:
                patterns_num_of_shortest_paths[next_town] = (patterns_num_of_shortest_paths[town] + patterns_num_of_shortest_paths[next_town]) % MOD

print(patterns_num_of_shortest_paths[N-1])