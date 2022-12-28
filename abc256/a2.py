X,Y,N = map(int,input().split())
ans = (N//3) * Y + (N%3) * X
ans = min(ans,X*N)
print(ans)