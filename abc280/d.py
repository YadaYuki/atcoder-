from collections import defaultdict
K = int(input())

def prime_factorize(n):
    a = defaultdict(int)
    while n % 2 == 0:
        a[2] += 1
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a[f] += 1
            n //= f
        else:
            f += 2
    if n != 1:
        a[n] += 1
    return a

d = prime_factorize(K)

ans = -1

for k,v in d.items():
    ans = max(k*v,ans)

print(ans)