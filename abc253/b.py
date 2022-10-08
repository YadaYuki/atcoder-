H,W = map(int,input().split())
S = [list(input()) for _ in range(H)]
# 
ab = []
for i in range(H):
    for j in range(W):
        if S[i][j] == "o":
            ab.append((i,j))



a,b = ab

xa,ya = a
xb,yb = b

ans = abs(xa-xb) + abs(ya-yb)

print(ans)


