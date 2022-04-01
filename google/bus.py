


def solve (N, Passengers, Edges):
    all_node_is_no_passenger = True
    for i in range(1,N):
        if Passengers[i] == 1:
            all_node_is_no_passenger = False
            break
    if all_node_is_no_passenger:
        return 0
    # Write your code here
    for edge in Edges:
        graph[edge[0]].append(edge[1])
        graph[edge[1]].append(edge[0])
    


    return dfs(-1,0)

def dfs(prev,cur):
    
    bus_count = 0
    for node_next in graph[cur]:
        if node_next != prev:
            bus_count += dfs(cur,node_next)
    
    if bus_count == 0 and Passengers[cur] == 1:
        bus_count = 1
    return bus_count
    
graph = None


T = int(input())
ans = []
for _ in range(T):
    N = int(input())
    Passengers = list(map(int, input().split()))
    Edges = [list(map(int, input().split())) for i in range(N-1)]
    graph = [[] for i in range(N)]

    out_ = solve(N, Passengers, Edges)
    print(out_)
    ans.append(out_)

