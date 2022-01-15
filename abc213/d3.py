import sys
sys.setrecursionlimit(10**6)

N = int(input())
graph = [[] for _ in range(N)]

for _ in range(N-1):
    A,B = map(int, input().split())
    graph[A-1].append(B-1)
    graph[B-1].append(A-1)

for i in range(N):
    graph[i] = sorted(graph[i])

ans = []


def dfs(prev,cur):
    for next in graph[cur]:
        if next != prev:
            ans.append(cur)
            dfs(cur,next)
            ans.append(next)


dfs(-1,0)

for city in ans:
    print(city+1,end=" ")

print(1,end=" ")