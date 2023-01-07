N,M,T = map(int,input().split())
A = list(map(int,input().split()))
bonus = [0 for i in range(N)]
for i in range(M):
    X,Y = map(int,input().split())
    X-=1
    bonus[X] = Y

for i,a in enumerate(A):
    # move i to i+1
    T -= a
    if T <= 0:
        print("No")
        exit()
    T += bonus[i+1]

print("Yes")