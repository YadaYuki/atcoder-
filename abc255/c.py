X,A,D,N = map(int,input().split())
last_val = A + D * (N-1)
min_val = min(A,last_val)
max_val = max(A,last_val)

if X <= min_val:
    print(min_val - X)
    exit()

if max_val < X:
    print(X - max_val)
    exit()

print(min(abs((X - A)%D),abs(D-(X-A)%D)))
