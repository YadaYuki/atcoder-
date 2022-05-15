def list_primes(limit):
    primes = []
    is_prime = [True] * (limit + 1)
    is_prime[0] = False
    is_prime[1] = False

    for p in range (0, limit + 1):
        if not is_prime[p]:
            continue
        primes.append(p)
        for i in range(p*p, limit + 1, p):
            is_prime[i] = False

    return primes


if __name__ == "__main__":
    N = int(input())
    prime_arr = list_primes(int(N**(1/3)))
    ans = 0
    for q in prime_arr:
        p_max = N // (q**3)
        ok,ng = -1,len(prime_arr)
        while abs(ok - ng) > 1:
            mid = (ok + ng) // 2
            if prime_arr[mid] <= p_max and prime_arr[mid] < q:
                ok = mid
            else:
                ng = mid
        ans += ok + 1
        

    print(ans)