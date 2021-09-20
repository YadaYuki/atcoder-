import sys
sys.setrecursionlimit(1000000)
N,M  = map(int,input().split())

edges = []

for i in range(N):
  edges.append([])

indeg = [0] * N

for i in range(M):
  x,y = list(map(int,input().split()))
  edges[x-1].append(y-1)
  indeg[y-1] += 1

lenght = [0] * N

done = [False] * N

def rec(i):
  if done[i]:
    return lenght[i]
  
  lenght[i] = 0

  for j in edges[i]:
    lenght[i] = max(lenght[i],rec(j) + 1)
  
  done[i] = True
  return lenght[i]

for i in range(N):
  if indeg[i] == 0:
    rec(i)

print(max(lenght))
