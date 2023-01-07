X,Y,N = map(int,input().split())
ans = min(X*N,(N//3)*Y + (N%3)*X)
print(ans)


