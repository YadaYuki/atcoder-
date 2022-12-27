N,M,T = map(int,input().split())
A = list(map(int,input().split()))
X,Y = list(),list()
bonus = [0 for i in range(N)]
for i in range(M):
    x,y = map(int,input().split())
    bonus[x-1] = y

for i,a in enumerate(A):
    T -= a
    if T <= 0:
        print("No")
        exit()
    T += bonus[i+1]

print("Yes")