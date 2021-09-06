import sys
sys.setrecursionlimit(100000)

H, W = map(int, input().split())
c = []
for i in range(H):
    c.append(input())

visited = [[False for _ in range(W)] for _ in range(H)]

si,sj,gi,gj = -1,-1,-1,-1

for i in range(H):
  for j in range(W):
    if c[i][j] == "s":
      si,sj = i,j
    if c[i][j] == "g":
      gi,gj = i,j

def dfs(i, j):
  for ij in [[i-1,j],[i,j-1],[i+1,j],[i,j+1]]:
    si,sj = ij
    if si < 0 or sj < 0 or si >= H or sj >= W:
      continue
    elif c[si][sj] == "#":
      continue
    elif visited[si][sj] == True:
      continue
    else:
      visited[si][sj] = True
      dfs(si,sj)

dfs(si,sj)

if visited[gi][gj] == True:
  print("Yes")
else:
  print("No")
       

