N,M,T = map(int,input().split())
A = list(map(int,input().split()))
bonus = [0 for i in range(N)]
for i in range(M):
    x,y = map(int,input().split())
    x-=1
    bonus[x] = y

time_to_arrive_N = 0

for i in range(N-1):
    time_to_arrive_N += A[i]
    T += bonus[i]

if time_to_arrive_N <= T:
    print("Yes")
else:
    print("No")

