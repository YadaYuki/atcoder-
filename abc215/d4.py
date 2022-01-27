N,M = map(int,input().split())

A = list(map(int,input().split()))

is_ans = [True] * (M+1)
checked_primes = [False] * (max(A)+1)

def trial_division(N:int):
    prime_factorization = []
    prime = 2
    while N > 1:
        if N % prime == 0:
            prime_factorization.append(prime)
            N //= prime
        else:
            prime += 1
        
    return prime_factorization


for i in range(N):
    prime_factorization_set = set(trial_division(A[i]))
    for prime in prime_factorization_set:
        if checked_primes[prime] != True:
            for j in range(prime,M+1,prime):
                is_ans[j] = False
            checked_primes[prime] = True


ans = [i for i in range(1,M+1) if is_ans[i] == True]

print(len(ans))
for i in range(len(ans)):
    print(ans[i])

