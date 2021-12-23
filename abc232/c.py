import copy
from itertools import permutations
from collections import defaultdict
N,M = map(int,input().split())

takahashi_toy = [[] for _ in range(N)]
aoki_toy = [[] for _ in range(N)]

for _ in range(M):
    a,b = map(int,input().split())
    takahashi_toy[a-1].append(b-1)
    takahashi_toy[b-1].append(a-1)


for _ in range(M):
    a,b = map(int,input().split())
    aoki_toy[a-1].append(b-1)
    aoki_toy[b-1].append(a-1)


    

def is_same_graph(g1,g2):
    for i in range(N):
        if len(g1[i]) != len(g2[i]):
            return False
        else:
            sorted_g1 = sorted(g1[i])
            sorted_g2 = sorted(g2[i])
            for j in range(len(g1[i])):
                if sorted_g1[j] != sorted_g2[j]:
                    return False
    return True

def convert_graph(graph,idx_arr):
    graph_copy = copy.deepcopy(graph)

    dic = defaultdict(bool)
    for i,idx in enumerate(idx_arr):
        min_i = min(idx,i)
        max_i = max(idx,i)
        key = f"{min_i},{max_i}"
        if idx != i and (not dic[key]):
            graph_copy[i],graph_copy[idx] = graph_copy[idx],graph_copy[i]
            dic[key] = True
    
    for i in range(N):
        for j in range(len(graph_copy[i])):
            graph_copy[i][j] = idx_arr[graph_copy[i][j]]
    
    return graph_copy



patterns = list(permutations([i for i in range(N)]))
print(patterns)
for P in patterns:
    takahashi_graph = convert_graph(takahashi_toy,P)
    if is_same_graph(takahashi_graph, aoki_toy):
        print("Yes")
        exit()

print("No")
