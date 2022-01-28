import math
from collections import defaultdict


def prime_factorization(n:int):
    square_root = int(math.sqrt(n))
    prime_factors = set()
    for i in range(2,square_root+1):
        if n%i == 0:
            ex = 0
            while n % i == 0:
                ex += 1
                n //=i

            prime_factors.add(i)
    if n > 1:
        prime_factors.add(n)
    return prime_factors


N,M = map(int,input().split())
A = list(map(int,input().split()))
primes = defaultdict(bool)
for i in range(N):
    square_root_i = int(math.sqrt(A[i]))
    n = A[i]
    for j in range(2,square_root_i+1):
        if n%j == 0:
            ex = 0
            while n % j == 0:
                ex += 1
                n //=j
            primes[j] = True
    if n > 1:
        primes[n] = True
ans = [1]

for i in range(2,M+1):
    square_root_i = int(math.sqrt(i))
    is_ans = True
    n = i
    for j in range(2,square_root_i+1):
        if n%j == 0:
            ex = 0
            while n % j == 0:
                ex += 1
                n //=j
            is_ans = not (j in primes)
    if n > 1:
        is_ans = not (n in primes)
    if is_ans:
        ans.append(i)

print(len(ans))
for i in range(len(ans)):
    print(ans[i])
             
            


