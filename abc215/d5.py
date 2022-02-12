N,M = map(int,input().split())
A = list(map(int,input().split()))
def prime_factorization(N:int):
    primes = []
    while N % 2 == 0:
        primes.append(2)
        N //= 2
    prime = 3
    while prime ** 2 <= N:
        if N % prime == 0:
            primes.append(prime)
            N //= prime
        else:
            prime += 2
    if N > 1:
        primes.append(N)    
    return primes


is_ans = [True] * (M+1)

for i in range(N):
    prime_factorization_set = set(prime_factorization(A[i]))
    for prime in prime_factorization_set:
        if prime <= M:
            if is_ans[prime]:
                for j in range(prime,M+1,prime):
                    is_ans[j] = False


ans = [i for i in range(1,M+1) if is_ans[i] == True]

print(len(ans))
for i in ans:
    print(i)
