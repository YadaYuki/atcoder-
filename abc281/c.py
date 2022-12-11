N,T = map(int,input().split())
A = list(map(int,input().split()))
A_sum = sum(A)
T %= A_sum

for i,a in enumerate(A):
    T -= a
    if T < 0:
        break
        
print(i+1,a+T)
