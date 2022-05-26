H,W = map(int,input().split())
R,C = map(int,input().split())
ans = 0
for r,c in [[R,C+1],[R,C-1],[R+1,C],[R-1,C]]:
    if 1<=r<=H and 1<=c<=W:
        ans += 1


print(ans)
