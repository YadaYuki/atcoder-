H,W,X,Y = map(int,input().split())

S = []

for i in range(H):
  S.append(list(input()))

# (x,y)の左側にある壁

left_side = -1

for i in range(Y):
  if S[X-1][i] == "#":
    left_side = i

right_side = W

for i in range(Y,W):
  if S[X-1][i] == "#":
    right_side = i
    break



top_side = -1

for i in range(X):
  if S[i][Y-1] == "#":
    top_side = i

down_side = H

for i in range(X,W):
  if S[i][Y-1] == "#":
    down_side = i
    break


print((right_side-left_side-1) + (down_side-top_side-1) - 1) # 1,5

