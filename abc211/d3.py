from collections import deque
N,M = map(int,input().split())
graph = [[] for _ in range(N)]

for _ in range(M):
    A,B= map(int,input().split())
    graph[A-1].append(B-1)
    graph[B-1].append(A-1)

min_cost_to_node = [-1] * N
pattenrns_num_of_shortest_paths = [0] * N
pattenrns_num_of_shortest_paths[0] = 1
min_cost_to_node[0] = 0
Q = deque([0])

MOD = 10**9+7

while len(Q) > 0:
    cur_node = Q.popleft()
    for node_next_to in graph[cur_node]:
        if pattenrns_num_of_shortest_paths[node_next_to] == 0 : #未訪問
            min_cost_to_node[node_next_to] = min_cost_to_node[cur_node] + 1
            pattenrns_num_of_shortest_paths[node_next_to] = pattenrns_num_of_shortest_paths[cur_node]
            Q.append(node_next_to)
        else:
            if min_cost_to_node[cur_node] + 1 == min_cost_to_node[node_next_to]:
                pattenrns_num_of_shortest_paths[node_next_to] =(pattenrns_num_of_shortest_paths[node_next_to]  +  pattenrns_num_of_shortest_paths[cur_node]) % MOD
            

print(pattenrns_num_of_shortest_paths[N-1])