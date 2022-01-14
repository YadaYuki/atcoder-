N = int(input())
A = list(map(int,input().split()))

if N % 2 == 1:
    print('Win')
    exit()

v = 0


for i in range(N):
     v ^= A[i]
for i in range(N):
    if v == A[i]:
        print('Win')
        exit()
    
print('Lose')
    
