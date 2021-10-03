N = int(input())
p = list(map(int, input().split()))

max_point = sum(p)

point = [[False for _ in range(max_point + 1)] for _ in range(N+1)]

# 0点はTrue(N = 0の時は,1点以上はFalse)
for i in range(N + 1):
    point[i][0] = True


for i in range(1,N+1):
  for j in range(1,max_point+1):
    point[i][j] = point[i-1][j]
    if j >= p[i-1]:
      if point[i-1][j-p[i-1]] == True:
        point[i][j] = True

print(sum(point[N]))

