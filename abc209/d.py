N,Q = map(int, input().split())

graph = [[] for _ in range(N)]

for _ in range(N-1):
    a,b = map(int, input().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)

query = []

for _ in range(N-1):
    a,b = map(int, input().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)