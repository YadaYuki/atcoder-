import math
def list_primes(n):
    is_primes = [True] * (n + 1)
    is_primes[0] = is_primes[1] = False
    for i in range(2, n+1):
        if is_primes[i]:
            for j in range(i*2, n+1, i):
                is_primes[j] = False
    
    primes = []

    for i in range(n+1):
        if is_primes[i]:
            primes.append(i)
    return primes


N = int(input())
q_max = math.floor(N ** (1/3))

primes = list_primes(q_max)

ans = 0
for q in primes:
    ok,ng = -1,len(primes)
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        p_candidate = primes[mid]
        k = q ** 3 * p_candidate
        if p_candidate < q and k <= N:
            ok = mid
        else:
            ng = mid
    ans += ok + 1

print(ans)