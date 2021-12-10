N,X = map(int,input().split())

A = list(map(int,input().split()))

sum_of_prices = 0

for i in range(N):
    if i% 2 == 1:
        A[i] = A[i] - 1
    sum_of_prices += A[i]

if sum_of_prices > X:
    print("No")
else:
    print("Yes")
