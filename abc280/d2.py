from math import gcd
K = int(input())

for i in range(1,2000001):
    K //= gcd(K,i)
    if K == 1:
        print(i)
        exit()

print(K)
