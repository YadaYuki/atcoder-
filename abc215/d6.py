N,M = map(int, input().split())
A = list(map(int, input().split()))

def prime_factorial(n):
    i = 2
    primes = []
    while n % 2 == 0:
        n //= 2
        primes.append(2)
    i = 3
    while i * i <= n:
        if n % i == 0:
            n //= i
            primes.append(i)
        else:
            i += 2
    
    if n > 1:
        primes.append(n)
    
    return primes




is_ans = [True] * (M+1)

for a in A:
    primes = prime_factorial(a)
    for p in primes:
        if p <= M:
            if is_ans[p]:
                for i in range(p,M+1,p):
                    is_ans[i] = False
    
ans = [i for i in range(1,M+1) if is_ans[i]]

print(len(ans))
for a in ans:
    print(a)